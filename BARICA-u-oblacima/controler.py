#!/usr/bin/env python3
from flask import Flask, Response, redirect, url_for, request, session, abort
from flask_login import LoginManager, UserMixin, \
                                login_required, login_user, logout_user
from flask_socketio import SocketIO

# install with
# sudo pip3 install git+https://github.com/AILab-FOI/pyxf
from pyxf.pyxf import *

from backendapi import load_modules

modules = load_modules()

app = Flask( __name__ )
socketio = SocketIO( app )

# flask-login
login_manager = LoginManager()
login_manager.init_app( app )
login_manager.login_view = "login"

# silly user model
# TODO: connect this to some DB
class User( UserMixin ):

    def __init__( self, id ):
        self.id = id
        self.name = "user" + str(id)
        self.password = self.name + "_secret"
        
    def __repr__( self ):
        return "%d/%s/%s" % ( self.id, self.name, self.password )


# create some users
# TODO: update this with data from DB
users = [ User( id ) for id in [ 'barica', 'ivek', 'joza', 'marica' ] ]


# REST API
@app.route( '/' )
@login_required
def index():
    return Response( '{"testing":"ok"}' )

# somewhere to login
@app.route( "/login", methods=[ "GET", "POST" ] )
def login():
    if request.method == 'POST':
        username = request.form[ 'username' ]
        password = request.form[ 'password' ]        
        if password == "test":
            id = username
            user = User( id )
            login_user( user )
            return redirect( request.args.get( "next" ) )
        else:
            return abort( 401 )
    else:
        login_html = open( 'html/login_form.html' ).read()
        return Response( login_html )


# somewhere to logout
@app.route( "/logout" )
@login_required
def logout():
    logout_user()
    return Response( '<p>Logged out</p>' )


# handle login failed
@app.errorhandler( 401 )
def page_not_found( e ):
    return Response( '<p>Login failed</p>' )
    
    
# callback to reload the user object        
@login_manager.user_loader
def load_user( userid ):
    return User( userid )
    

# WS API

# Testing
@app.route( "/wsapi-test" )
@login_required
def wstest():
    page = open( 'html/wsapi-test.html' ).read()
    print( page )
    return Response( page )


@socketio.on( 'json' )
def handle_json( json ):
    print( 'received json: ' + str( json ) )


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

    SERVERNAME = "%s:%d" % ( args.ip, args.port )

    # config
    app.config.update(
        DEBUG = True,
        SECRET_KEY = 'baricajezakon321$$$',
        SERVER_NAME=SERVERNAME
    )

    #socketio.run( app )
    app.run()
