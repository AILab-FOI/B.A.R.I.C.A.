#!/usr/bin/env python3

from flask import Flask, Response, redirect, flash, url_for, request, session, abort
from flask import render_template
from flask_login import LoginManager, UserMixin, \
                                login_required, login_user, current_user, logout_user
from werkzeug.urls import url_parse

import json, io
from time import sleep
from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket
import _thread


# install with
# sudo pip3 install git+https://github.com/AILab-FOI/pyxf
from pyxf.pyxf import *

from backendapi import load_modules, StreamPortManager, set_IP
from slackapi import run


#database module
from database import app, db, Config
from database.models import DBUser, DBRole # old type user class and new one for database


# flask-login
login_manager = LoginManager()
login_manager.init_app( app )
login_manager.login_view = "login"


# if no user exists, this create Barica - test user
def prepare_database():
    user = DBUser.query.filter(DBUser.id==1).first()
    role = DBRole.query.filter(DBRole.id==1).first()
    res = ""
    if role == None: #there must be first role
        role = DBRole(id=1, role="admin")
        db.session.add(role)
        db.session.commit()
    elif role.role != "admin": #first role in database must be admin
        db.session.delete(role)
        role = DBRole(id=1, role="admin")
        db.session.commit()
    if user == None: #first user is test user Barica
        user = DBUser(id=1, name="Barica", role_id=1)
        user.set_password("test")
        db.session.add(user)
        db.session.commit()
        res = "<p>No default user.</p><p>Refresh to create default user</p>"
    else:
        if user.check_password("test") == False:
            user.set_password("test")
        output = io.StringIO()
        #join two tables: users and roles
        user2 = DBUser.query.join(DBRole, DBUser.role_id==DBRole.id).\
        add_columns(DBUser.id,DBUser.name,DBRole.role,DBUser.password_hash).\
        filter(DBUser.id==1).first()
        print("Test - name: {0:s} - role: {1:s}, password: test".format(user2.name, user2.role), file=output)
        res = output.getvalue()
        output.close()
    return res


# Admin site
@app.route( '/' )
@app.route( '/index' )
@login_required
def index():
    #prepare database - test user
    print("Current user: {}".format(current_user.name))
    

    # TODO: Put here an administrative site for logged in users
    # including an introspection of available modules and methods.
    return render_template('index.html',title="Index", hint="testing: ok")
    #return Response( '{"testing":"ok"}' )

# Login form for the administrative site
@app.route( "/login", methods=[ "GET", "POST" ] )
def login():
    title = "Login"
    hint = prepare_database()

    if request.method == 'POST':

        username = request.form[ 'username' ]
        password = request.form[ 'password' ]  
        user1 = DBUser.query.filter(DBUser.name==username).first()
        if user1 != None:
            if user1.password_hash != None:
                if user1.check_password(password) == True: 
                    login_user (user1) 
                    next_page = request.args.get('next')
                    if not next_page or url_parse(next_page).netloc != '':
                        next_page = '/index'

                    return redirect (next_page)
                else:
                    return abort( 401 )
            else:
                return abort ( 401 )
        else:
            return abort( 401 )

    else:
        # TODO: make this look better
        return render_template('login_form.html',title=title,hint=hint)

        #login_html = open( 'html/login_form.html' ).read()
        #return Response( login_html )


# Logout method
@app.route("/logout")
@login_required
def logout():
    logout_user()
    # TODO: Make this look better
    return render_template('logout.html',title="Logout",hint="Logged out")
    #return Response( '<p>Logged out</p>' )

# User registration
@app.route("/register", methods=[ "GET", "POST" ] )
def register_user():
    if current_user.is_authenticated:
        return redirect("/index")
    hint = ""
    if request.method == 'POST':
        username = request.form[ 'username' ]
        password1 = request.form[ 'password1' ]  
        password2 = request.form[ 'password2' ] 
        if username == "":
            hint = "No username."
        elif password1 == "":
            hint = "No password."
        elif password1 != password2:
            hint = "No passwords match."
        else:
            user = DBUser.query.filter(DBUser.name==username).first()
            if user != None:
                hint = "User with that username exists."
        if hint != "":
            return render_template('registration.html',title="Registration",hint=hint)
        else:
            user = DBUser(name = username)
            user.set_password( password1 )
            db.session.add(user)
            db.session.commit()
            flash('Congratulations, you are now a registered user!')
            next_page = request.args.get('next')
            if not next_page or url_parse(next_page).netloc != '':
                next_page = '/login'
            return redirect (next_page)
    else:
        return render_template('registration.html',title="Registration",hint=hint)


# handle login failed
@app.errorhandler( 401 )
def page_not_found( e ):
    return render_template('error.html',title="Error",hint="Login failed")
    #return Response( '<p>Login failed</p>' )
    


@login_manager.user_loader
def load_user(user_id):
    user = DBUser.query.filter(DBUser.id==user_id).first()
    if user != None:
        print("Load user callback: {0}: {1}".format(user.id, user.name))
    else:
        print("Load user callback: None")
    return user
   

# REST API
# Running module method
# Add authentication
@app.route( "/ask/<query>" )
def ask( query ):
    q = json.loads( query )
    return Response( modules[ q[ "module" ] ].run( q[ "method" ], q[ "args" ] ) )

 

# WS API

# Global message buffer
BUFFER = []
class WSController( WebSocket ) :
    def __init__( self, *args, **kwargs ):
        WebSocket.__init__( self, *args, **kwargs )
        _thread.start_new_thread( self.listen, () )
        
    def listen( self ):
        # To send push messages to clients just add message to
        # BUFFER
        # message format { "data":data, "address":address }
        # data is JSON encoded
        # address is a host:port tuple (e.g. ('127.0.0.1', 46428) )
        global BUFFER
        while True:
            try:
                if BUFFER:
                    if BUFFER[ 0 ][ "address" ] == self.address:
                        msg = BUFFER.pop()
                        print( 'Sending', str( msg[ "data" ] ) )
                        self.sendMessage( json.dumps( json.loads( msg ) ) )
                        sleep( 0.5 )
            except Exception as e:
                print( 'WSController: There was an error!', e )

    def handleMessage( self ):
        # TODO: Add authentication here!
        print( self.data )
        if self.data != 'connect':
            data = json.loads( self.data )
            result = modules[ data[ "module" ] ].run( data[ "method" ], data[ "args" ] )
            self.sendMessage( json.dumps( json.loads( result ) ) )
        else:
            self.sendMessage( 'connect' )

    def handleConnected( self ):
        print( self.address, 'connected' )
        
    def handleClose( self ):
        print( self.address, 'closed' )

# Testing
@app.route( "/wsapi-test" )
def wstest():
    page = open( 'html/wsapi-test.html' ).read()
    return Response( page )

def slack_handler( command, channel ):
    if command.startswith( "do" ):
        response = "Sure...write some more code then I can do that!"
    else:
        response = "Sorry, cannot answer yet. Check back later when I am implemented!"
    return response

_thread.start_new_thread( run, ( slack_handler, ) )

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument( "--ip", const=True, nargs='?', type=str, help="Specify the IP address of the server.")
    parser.add_argument( "--port", const=True, nargs='?', type=int, help="Specify the port of the server.")
    args = parser.parse_args()

    
    if not args.ip:
        args.ip = '127.0.0.1'
    if not args.port:
        args.port = 5000

    set_IP( args.ip )
    modules = load_modules()

    SERVERNAME = "%s:%d" % ( args.ip, args.port )

    WSPORT = 8001
    

    # config
    app.config.update(
        DEBUG = False,
        SERVER_NAME=SERVERNAME
    )


    server = SimpleWebSocketServer( '', WSPORT, WSController )
    _thread.start_new_thread( server.serveforever, () )

    
    spm = StreamPortManager( 10 )
    spm.start()


    app.run() # ssl_context='adhoc' (add this for HTTPS)

    print("App run exit")
    spm.stop()
    spm.join()
