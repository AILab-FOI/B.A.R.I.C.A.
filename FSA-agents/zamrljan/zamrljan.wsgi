import sys, os

FOLDER = '/home/markus/agenti-fsa/zamrljan'

sys.path.insert( 0, FOLDER )
import _thread
from SimpleWebSocketServer import SimpleSSLWebSocketServer
from chatterbot import ChatBot
from server import NLPController, app as application

#server = SimpleSSLWebSocketServer('localhost', 8009, NLPController, '/home/markus/agenti-fsa/server/keys/fullchain.pem', '/home/markus/agenti-fsa/server/keys/privkey.pem')

#_thread.start_new_thread( server.serveforever, () )
