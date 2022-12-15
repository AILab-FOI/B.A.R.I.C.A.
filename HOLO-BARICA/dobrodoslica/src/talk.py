#!/usr/bin/env python3
#-*- coding: utf-8 -*-

from time import sleep

import subprocess

import _thread

import sys

from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket

from collections import OrderedDict

import argparse

from random import choice, randint

# Global vars

# Global state
STATE = 'IDLE'

# Last sentence
SENTENCE = ''

# Command from chatbot
CMD = ''

# Websocket communication buffer (e.g. messages to be sent)
BUFFER = []

# Last random sentence
LAST = ''



class NLPController( WebSocket ) :
	def __init__( self, *args, **kwargs ):
		WebSocket.__init__( self, *args, **kwargs )
		_thread.start_new_thread( self.listen, () )

	def listen( self ):
		global BUFFER
		while True:
			try:
				if BUFFER:
					BUFFER = list( OrderedDict.fromkeys( BUFFER ) )
					print( 'BUFFER:', BUFFER )
					cmd = BUFFER.pop()
					print( 'Sending', str( cmd ) )
					self.sendMessage( str( cmd ) )
				sleep( 0.5 )
			except Exception as e:
				print( 'NLPController: There was an error!', e )

	def handleMessage( self ):
		print( self.data )
		self.sendMessage( self.data )

	def handleConnected(self):
		print( self.address, 'connected' )

	def handleClose( self ):
		print( self.address, 'closed' )
		sys.exit()



def rnd_change():
	global STATE
	while True:
		STATE = 'ACTIVE'
		sleep_time = randint( 2, 10 )
		print( 'Sleeping', sleep_time )
		sleep( sleep_time )
		STATE = 'IDLE'
		sleep( sleep_time )


if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument( "--train", const=True, nargs='?', type=bool, help="Specify if the agent shoud be trained. If not specified agent will be started in default (listening) mode.")
	args = parser.parse_args()

	TRAIN = bool( args.train )

	server = SimpleWebSocketServer( '', 8009, NLPController )
	_thread.start_new_thread( server.serveforever, () )

	# simulate trigger
	_thread.start_new_thread( rnd_change, () )

	t = 0
	ans = ''
	while True:
		BUFFER = list( OrderedDict.fromkeys( BUFFER ) )
		print( 'BUFFER:', BUFFER )

		msgs = [ 'dobrodosli',
			 'dobrodosli na dan fakulteta',
			 'lijepo vas je vidjeti',
			 'dobrodosli na dan FOI',
			 'dobar dan, dobrodosli',
			 'kako ste',
			 'drago mi je vas pozdraviti' ]

		if STATE == 'IDLE':
			pass
		elif STATE == 'ACTIVE':
			nxt = choice( msgs )
			while nxt == LAST:
				nxt = choice( msgs )
			BUFFER.append( nxt )
			sleep( 5 )
			LAST = nxt

		sleep( 0.5 )
