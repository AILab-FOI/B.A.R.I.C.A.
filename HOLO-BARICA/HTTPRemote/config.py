#!/usr/bin/env python
import autopy

# Config 

# Games config

# Abe

abe_game = {
	"title":"Abe's Amazing Adventure",
	"players":1,
	"executable":"/usr/games/abe",
	'toggles':[ 'UP', 'DOWN', 'LEFT', 'RIGHT' ],
	'taps':[ 'SELECT', 'START', 'A', 'B' ],
	"description":"""A scrolling, platform-jumping, key-collecting, ancient pyramid exploring game, vaguely in the style of similar games for the Commodore+4. The game is intended to show young people (I'm writing it for my son's birthday) all the cool games they missed.""",
	"website":"abe.sourceforge.net",
	"developer":"Gabor Torok",
	"controls": [
		{
		  'UP':autopy.key.K_UP,
		  'DOWN':autopy.key.K_DOWN,
		  'LEFT':autopy.key.K_LEFT,
		  'RIGHT':autopy.key.K_RIGHT,
		  'SELECT':autopy.key.K_ESCAPE,
		  'START':autopy.key.K_RETURN,
		  'A':' ',
		  'B':' '
		}
	]
}

supertuxkart_game = {
	"title":"SuperTuxKart",
	"players":4,
	"executable":"/usr/games/supertuxkart",
	'toggles':[ 'UP', 'DOWN', 'LEFT', 'RIGHT' ],
	'taps':[ 'SELECT', 'START', 'A', 'B' ],
	"description":"""Karts. Nitro. Action! SuperTuxKart is a 3D open-source arcade racer with a variety characters, tracks, and modes to play. Our aim is to create a game that is more fun than realistic, and provide an enjoyable experience for all ages.

In Story mode, you must face the evil Nolok, and defeat him in order to make the Mascot Kingdom safe once again! You can race by yourself against the computer, compete in several Grand Prix cups, or try to beat your fastest time in Time Trial mode. You can also race with up to four friends on one PC, or battle each other in multiplayer arenas.""",
	"website":"www.supertuxkart.net",
	"developer":"SuperTuxKart Team",
	"controls": [
		{
		  'UP':autopy.key.K_UP,
		  'DOWN':autopy.key.K_DOWN,
		  'LEFT':autopy.key.K_LEFT,
		  'RIGHT':autopy.key.K_RIGHT,
		  'SELECT':autopy.key.K_ESCAPE,
		  'START':autopy.key.K_RETURN,
		  'A':' ',
		  'B':'n'
		},
		{
		  'UP':'w',
		  'DOWN':'s',
		  'LEFT':'a',
		  'RIGHT':'d',
		  'SELECT':'q',
		  'START':'e',
		  'A':'x',
		  'B':'y'
		}
	]
}

# Controller toggles (keys)

games = {
	"abe":abe_game,
	"supertuxkart":supertuxkart_game
}

# Network manager config file
nm_config = "/etc/NetworkManager/NetworkManager.conf"

# Address and port 
# TODO: Change this later to DNS entries 
ADDR_OUT = '192.168.12.1'
PORT = 2727

ADDR = '0.0.0.0'

# Application options (for templates, AP etc.)
APP_OPTS = {
	'version':'0.3',
	'program': 'brain4 GAMES',
	'ssid': 'brain4games',
	'wifipass': 'braindrain',
	'upload_path': 'uploads/',
	'user':'markus'
}

# Session management options
''' OVAJ DIO KASNIJE ZA REGISTRACIJU '''
SESSION_OPTS = {
	'session.type': 'file',
	'session.cookie_expires': 300,
	'session.data_dir': './sessions',
	'session.auto': True
}
