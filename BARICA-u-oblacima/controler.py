#!/usr/bin/env python3

from flask import Flask, Response, redirect, url_for, request, session, abort
from flask import render_template
from flask_login import LoginManager, UserMixin, \
                                login_required, login_user, logout_user


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
from database.models import User, DBUser # old type user class and new one for database


# flask-login
login_manager = LoginManager()
login_manager.init_app( app )
login_manager.login_view = "login"

# silly user model
# TODO: connect this to some DB

'''
class User( UserMixin ):

    def __init__( self, id ):
        self.id = id
        self.name = "user" + str(id)
        self.password = self.name + "_secret"
        
    def __repr__( self ):
        return "%d/%s/%s" % ( self.id, self.name, self.password )
'''

# create some users
# TODO: update this with data from DB
users = [ User( id ) for id in [ 'barica', 'ivek', 'joza', 'marica' ] ]

def prepare_database():
    user = DBUser.query.filter_by(id=1).first()
    res = ""
    if user == None:
        user = DBUser(id=1, name="Barica")
        user.set_password("test")
        db.session.add(user)
        db.session.commit()
        res = "<p>No default user.</p><p>Refresh to create default user</p>"
    else:
        if user.check_password("test") == False:
            user.set_password("test")
        output = io.StringIO()
        print("Test - name: {0:s}, password: test".format(user.name), file=output)
        res = output.getvalue()
        output.close()
    return res


# Admin site
@app.route( '/' )
@login_required
def index():
    #prepare database - test user
    

    # TODO: Put here an administrative site for logged in users
    # including an introspection of available modules and methods.
    return Response( '{"testing":"ok"}' )

# Login form for the administrative site
@app.route( "/login", methods=[ "GET", "POST" ] )
def login():
    title = "Login"
    hint = prepare_database()
    

    if request.method == 'POST':

        username = request.form[ 'username' ]
        password = request.form[ 'password' ]    

        user2 = DBUser.query.filter_by(name=username).first()
        if user2 != None:
            if user2.password_hash != None:
                print("User - id: {0:d}, name: {1:s}, pass hash: {2:s}".format(user2.id, user2.name, user2.password_hash))
                if user2.check_password(password) == True:
                    login_user (user2)
                    return redirect (request.args.get( "next" ))
                else:
                    return abort( 401 )
            else:
                print("User - id: {0:d}, name: {1:s}, pass hash: None".format(user2.id, user2.name))
                return abort ( 401 )
        else:
            return abort( 401 )

    else:
        # TODO: make this look better
        return render_template('login_form.html',title=title,hint=hint)

        #login_html = open( 'html/login_form.html' ).read()
        #return Response( login_html )


# Logout method
@app.route( "/logout" )
@login_required
def logout():
    logout_user()
    # TODO: Make this look better
    return Response( '<p>Logged out</p>' )


# handle login failed
@app.errorhandler( 401 )
def page_not_found( e ):
    return Response( '<p>Login failed</p>' )
    
    
# callback to reload the user object        
@login_manager.user_loader
def load_user( userid ):
    return User( userid )
   

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
