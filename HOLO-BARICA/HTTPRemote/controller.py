#!/usr/bin/env python
# includes
import bottle as bo
from beaker.middleware import SessionMiddleware
from time import sleep 
import subprocess
import threading
from gevent.pywsgi import WSGIServer
from geventwebsocket import WebSocketError
from geventwebsocket.handler import WebSocketHandler
from json import loads
import os
from time import sleep
from config import *
import eyed3
from glob import glob
import sqlite3

# GLOBAL VARIABLES

# How many players/clients are currently connected to a game
PLAYERS = 0
GAME_STARTED = False

# FUNCTIONS

def game_done():
	global PLAYERS, GAME_STARTED
	PLAYERS = 0
	GAME_STARTED = False

def popenAndCall( onExit, *popenArgs ):
	"""
	Runs the given args in a subprocess.Popen, and then calls the function
	onExit when the subprocess completes.
	onExit is a callable object, and popenArgs is a list/tuple of args that 
	would give to subprocess.Popen.

	Adapted from: http://stackoverflow.com/questions/2581817/python-subprocess-callback-when-cmd-exits
	"""

	def runInThread( onExit, *popenArgs ):
		proc = subprocess.Popen( *popenArgs )
		proc.wait()
		onExit()
		return
	thread = threading.Thread( target=runInThread, args=( onExit, popenArgs ) )
	thread.start()
	# returns immediately after the thread starts
	return thread

def unique_file( path, fname ):
	# Create a unique file name on the given path
	# for the given file name
	ext = os.path.splitext( fname )[ 1 ]
	if path[ -1 ] != '/':
		path += '/'
	pattern = path + '*' + ext
	files = glob( pattern )
	if files:
		num = max( [ int( f.split( '/' )[ -1 ][ :4 ] ) for f in files ] )
		num += 1
		return path + '%04d_' % num + fname
	else:
		return path + '0000_' + fname

def list_mp3s( path ):
	# List all mp3 files in a given path
	if path[ -1 ] != '/':
		path += '/'
	pattern = path + '*.mp3'
	mp3s = glob( pattern )
	descriptors = []
	mp3s.sort()
	for mp3 in mp3s:
		song = {}
		song[ "num" ] = int( mp3.split( '/' )[ -1 ][ :4 ] )
		fl = eyed3.load( mp3 )
		song[ "artist" ] = fl.tag.artist
		song[ "title" ] = fl.tag.title
		seconds = fl.info.time_secs
		m, s = divmod( seconds, 60 )
		h, m = divmod( m, 60 )
		if h > 0:
			song[ "duration" ] = "%d:%02d:%02d" % ( h, m, s )
		else:
			song[ "duration" ] = "%02d:%02d" % ( m, s )
		descriptors.append( song )
	return descriptors

# TODO: delete this after session management is implemented
@bo.route('/test')
def test():
  s = bo.request.environ.get('beaker.session')
  s['test'] = s.get('test',0) + 1
  s.save()
  return 'Test counter: %d' % s['test']

# Websocket controller
# TODO: map controls depending on various games that are played and players
@bo.route('/wsgc')
def handle_websocket():
	wsock = bo.request.environ.get( 'wsgi.websocket' )
	if not wsock:
		bo.abort( 400, 'Expected WebSocket request.' )
		return

	global PLAYERS, GAME_STARTED

	PLAYERS += 1

	while True:
		try:

			if not GAME_STARTED:
				print 'Game aborted or not started! Player', PLAYERS
				bo.abort( 400, "Game hasn't started or stopped running!" )
				break

			message = wsock.receive()
			try:
				msg = loads( message )
			except:
				print "Error while loading message:", message
				bo.abort( 400, 'Your browser sent an unparsable message.' )
				break
			cmd = msg[ "cmd" ]
			context = msg[ "context" ]
			game = msg[ "game" ]

			if PLAYERS > games[ game ][ "players" ]:
				print "To many players! Player", PLAYERS
				bo.abort( 400, 'To many players already connected for this game.' )
				break

			# TODO: add controls for other players
			try:
				toggles = games[ game ][ "controls" ][ PLAYERS - 1 ]
			except:
				print "Error, unknown game! Player", PLAYERS
				return "Error! Unknown game!"
			
			val = context == "start"
		
			for k in toggles.keys():
				if k != cmd and cmd not in games[ game ][ 'taps' ]:
					if cmd in ( 'UP', 'DOWN' ) and k in ( 'LEFT', 'RIGHT' ):
						continue
					if cmd in ( 'LEFT', 'RIGHT' ) and k in ( 'UP', 'DOWN' ):
						continue
					autopy.key.toggle( toggles[ k ], False )
		
			if cmd in games[ game ][ 'taps' ]:
				autopy.key.tap( toggles[ cmd ] )
			elif cmd in games[ game ][ 'toggles' ]:
				autopy.key.toggle( toggles[ cmd ], val )
			
			print 'Player',PLAYERS,'Got',cmd,context
				
		except WebSocketError:
			print "Web socket error for player", PLAYERS
			PLAYERS -= 1
			break

# Static files 

# Manifest
@bo.route("/manifest.json")
def manifest():
	return bo.static_file("templates/manifest.json")

# Images
@bo.route("/images/<filepath:re:.*>")
def images( filepath ):
	return bo.static_file(filepath, root="images")

# Templates
@bo.route("/template/<filepath:re:.*>")
def templates( filepath ):
	return bo.static_file(filepath, root="template")

# JavaScripts
@bo.route("/js/<filepath:re:.*>")
def js( filepath ):
	return bo.static_file(filepath, root="js")

# Other assets and static files
@bo.route("/assets/<filepath:re:.*>")
def assets( filepath ):
	return bo.static_file(filepath, root="assets")

# Index (main menu)
@bo.route('/')
def index():
	return bo.template( "templates/index.tpl", **APP_OPTS )

# Music (menu)
@bo.route('/music')
def music():
	playlist = list_mp3s( APP_OPTS[ 'upload_path' ] )
	APP_OPTS[ 'playlist' ] = playlist
	return bo.template( "templates/music.tpl", **APP_OPTS )

# Games (menu)
@bo.route('/games')
def music():
	global games
	APP_OPTS[ 'games' ] = games
	return bo.template( "templates/games.tpl", **APP_OPTS )

# Motion test
# TODO: Implement this into game controller
@bo.route('/motion')
def music():
	global GAME_STARTED, PLAYERS
	if not GAME_STARTED:
		GAME_STARTED = True
		PLAYERS = 0
		#popenAndCall( game_done, games[ "supertuxkart" ][ "executable" ] )
	return bo.template( "templates/motion.tpl", wsadd='ws://' + ADDR_OUT + ":" + str( PORT ) + '/wsgc', game="supertuxkart" )

# Games

# Start game
@bo.route( '/game/<game>/start' )
def start_game( game ):
	global GAME_STARTED, PLAYERS
	if not GAME_STARTED:
		GAME_STARTED = True
		PLAYERS = 0
		popenAndCall( game_done, games[ game ][ "executable" ] )
	return bo.template( "templates/ctrl.tpl", wsadd='ws://' + ADDR_OUT + ":" + str( PORT ) + '/wsgc', game=game )

# Upload mp3 form
# TODO: Add this to music template
@bo.route( '/upload/mp3' )
def upload_mp3():
	return '''<form action="/upload/mp3/do" method="post" enctype="multipart/form-data">
  Select a file: <input type="file" name="upload" />
  <input type="submit" value="Start upload" />
</form>'''

# Upload and play mp3 file
@bo.route('/upload/mp3/do', method='POST')
def do_upload():
	upload = bo.request.files.get( 'upload' )
	name, ext = os.path.splitext(upload.filename)
	if ext not in ('.mp3'):
		return "Only mp3 files are allowed."

	save_path = APP_OPTS[ 'upload_path' ]
	if not os.path.exists(save_path):
		os.makedirs(save_path)

	file_path = unique_file( save_path, upload.filename )
	#file_path = "{path}/{file}".format(path=save_path, file=upload.filename)
	try:
		upload.save(file_path)
	except Exception as e:
		print 'Error uploading file: ', e
	
	tag = eyed3.load( file_path ).tag
	print tag.artist, ':', tag.title
	subprocess.Popen( [ 'play', file_path ] )
	subprocess.Popen( [ 'projectM-pulseaudio' ] )
	sleep( 3 )
	autopy.key.tap( 'f' )
	return "File successfully saved to '{0}'<br /> Playing now!.".format(save_path)

# Stop music
@bo.route( '/stop/music' )
def stop_music():
	subprocess.Popen( [ 'killall', 'play' ] )
	subprocess.Popen( [ 'killall', '-s', 'SIGKILL', 'projectM-pulseaudio' ] )

if __name__ == '__main__':
	try:
		# Start the hotspot
		print 'Starting the hotspot ...',
		subprocess.Popen( [ 'create_ap', '-n', 'wlan0', '--no-virt', APP_OPTS[ 'ssid' ], APP_OPTS[ 'wifipass' ] ] )
		print 'done!'
		# Start the server
		print 'Starting server ...'
		app = SessionMiddleware( bo.app(), SESSION_OPTS )
		server = WSGIServer( ( ADDR, PORT ), app, handler_class=WebSocketHandler)
		server.serve_forever()
	except KeyboardInterrupt:
		# Restore NetworkManger config
		print 'Server stopped. Cleaning up ...',
		config_file = open( nm_config )
		new_config = []
		for line in config_file.readlines():
			if line != '[keyfile]\n' and not line.startswith( 'unmanaged-devices' ):
				new_config.append( line )

		new_config = ''.join( new_config ).rstrip()
		
		config_file.close()
		print 'done!'
		config_file = open( nm_config, 'w' )
		config_file.write( new_config )
			
