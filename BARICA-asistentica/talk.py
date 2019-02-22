#!/usr/bin/env python3
#-*- coding: utf-8 -*-

from time import sleep

import subprocess

import _thread

import sys

import pyperclip as cp

from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket

from pyautogui import press

from chatterbot import ChatBot

from collections import OrderedDict

import argparse

from random import choice

# Global vars

# Global state
STATE = 'IDLE'

# Last sentence
SENTENCE = ''

# Command from chatbot
CMD = ''

# Interface language
LANG = 'HR'

# Timeout in alert mode
TIMEOUT = 15

# Websocket communication buffer (e.g. messages to be sent)
BUFFER = []

MSGS_EN = {
	'Computer':'computer',
	'Talk to me':'talk to me',
	'Stop talking':'stop talking',
	'Start games':'start game',
	'Start animation':'start animation',
	'Go idle':'go idle',
	'Yes?':'yes?',
	'Starting game!':'starting game!',
	"Yes, I'm listening":"Yes, I'm listening!",
	'Change slide':"change slide",
	'AI speech':"AI speech",
	'speech':"speech"
}

MSGS_HR = {
	'Computer':'barice',
	'Talk to me':'pričaj sa mnom',
	'Stop talking':'prestani pričat',
	'Start games':'pokreni igru',
	'Start animation':'pokreni animaciju',
	'Go idle':'spavaj',
	'Yes?':'da?',
	'Starting game!':'pokrećem igru!',
	"Yes, I'm listening":"U redu, slušam!",
	'Change slide':"sljedeći slajd",
	'AI speech':"AI govor",
	'speech':"govor"
}

MSGS_DE = {
	'Computer':'computer',
	'Talk to me':'sprich mit mir',
	'Stop talking':'leise sein',
	'Start games':'ich will spielen',
	'Start animation':'starte animation',
	'Go idle':'schlaf',
	'Yes?':'ja?',
	'Starting game!':'starte Spiel!',
	"Yes, I'm listening":"Ja, ich höre!",
	'Change slide':"nächster slide",
	'AI speech':"AI rede",
	'speech':"govor"
}

MESSAGES = {
	'EN':MSGS_EN,
	'DE':MSGS_DE,
	'HR':MSGS_HR
}

LANGS = {
	'EN':'english',
	'DE':'german',
	'HR':'croatian'
}




def say( msg ):
	global LANGS, LANG, SENTENCE
	old = SENTENCE
	'''proc = subprocess.Popen( ['espeak', '-v', LANGS[ LANG ], "-g", "12", "-a", "200", "-s", "120", "-p", "99", '"' + msg.replace( '"', "'" ) + '"' ] )
	proc.wait()'''
	BUFFER.append( msg.replace( '"', "'" ) )
	sleep( 0.5 )
	cp.copy( old )

def listen():
	global SENTENCE, CMD
	sleep( 0.5 )
	l = cp.paste().lower()
	print( 'Heard:', l )
	if l != SENTENCE:
		SENTENCE = l
	else:
		CMD = ''


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





if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument( "--train", const=True, nargs='?', type=bool, help="Specify if the agent shoud be trained. If not specified agent will be started in default (listening) mode.")
	args = parser.parse_args()

	TRAIN = bool( args.train )

	chatbot = ChatBot( 'BARICA_HR', read_only=not TRAIN )

	if TRAIN:
		from train import *
		train( chatbot )
		sys.exit()

	server = SimpleWebSocketServer( '', 8009, NLPController )
	_thread.start_new_thread( server.serveforever, () )	

	t = 0
	ans = ''
	MSGS = MESSAGES[ LANG ]
	while True:
		BUFFER = list( OrderedDict.fromkeys( BUFFER ) )
		print( 'BUFFER:', BUFFER )
		listen()
		t += 1
		print( "STATE:", STATE )
		if SENTENCE:
			CMD = chatbot.get_response( SENTENCE )
		print( "CMD:", CMD )
		if STATE == 'IDLE':
			if SENTENCE == MSGS[ 'Computer' ] or CMD == 'Da?':
				STATE = 'ALERT MODE'
				tx = t
				say( MSGS[ 'Yes?' ] )
		elif STATE == 'ALERT MODE':
			if tx + TIMEOUT == t:
				STATE = 'IDLE'
				CMD == ''
			elif SENTENCE == MSGS[ 'Go idle' ]:	
				STATE = 'IDLE'
			elif SENTENCE == MSGS[ 'Change slide' ] or CMD == 'slide':	
				STATE = 'SLIDE'
			elif SENTENCE == MSGS[ 'Start animation' ] or CMD == 'animiraj':	
				STATE = 'ANIMATION'
			elif SENTENCE == MSGS[ 'AI speech' ] or CMD == 'govor':	
				STATE = 'AISPEECH'
			elif CMD == 'nema_na_cemu':
				STATE = 'YOU_RE_WELLCOME'
			elif CMD == 'predstavljanje':
				STATE = 'INTRODUCTION'
			elif CMD == 'cool_projekti':
				STATE = 'COOL_PROJECTS'
			elif CMD == 'ucite':
				STATE = 'LEARN'
		elif STATE == 'DO CMD':
			start_game()
			STATE = 'IDLE'
		elif STATE == 'SLIDE':
			press( ' ' )
			STATE = 'IDLE'
		elif STATE == 'ANIMATION':
			moze = choice( [ 'dakako', 'moze', 'za vas uvijek', 'nema problema' ] )
			BUFFER.append( moze )
			sleep( 1 )
			for i in range( 7 ):
				press( ' ' )
				sleep( 15 )
			STATE = 'IDLE'
		elif STATE == 'AISPEECH':
			BUFFER.append( 'govor' )
			sleep( 1 )
			press( ' ' )
			sleep( 11 )
			press( ' ' )
			sleep( 13 )
			press( ' ' )
			sleep( 6 )
			press( ' ' )
			STATE = 'IDLE'
		elif STATE == 'YOU_RE_WELLCOME':
			zahvala = choice( [ 'nema na cemu', 'za vas uvijek' ] )
			BUFFER.append( zahvala )
			sleep( 1 )
			STATE = 'IDLE'
		elif STATE == 'INTRODUCTION':
			BUFFER.append( 'predstavljanje' )
			sleep( 5 )
			STATE = 'IDLE'
		elif STATE == 'COOL_PROJECTS':
			BUFFER.append( 'cool projekti' )
			sleep( 2 )
			STATE = 'IDLE'
		elif STATE == 'LEARN':
			BUFFER.append( 'ucite' )
			sleep( 2 )
			STATE = 'IDLE'
			
				
