import sys, os

FOLDER = '/home/markus/agenti-fsa/micko'

sys.path.insert( 0, FOLDER )
#import _thread
from SimpleWebSocketServer import SimpleSSLWebSocketServer
from chatterbot import ChatBot
from server import NLPController #, app as application

server = SimpleSSLWebSocketServer('localhost', 8014, NLPController, '/home/markus/agenti-fsa/micko/keys/fullchain.pem', '/home/markus/agenti-fsa/micko/keys/privkey.pem')
server.serveforever()

#_thread.start_new_thread( server.serveforever, () )

