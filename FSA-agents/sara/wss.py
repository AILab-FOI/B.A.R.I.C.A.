import sys, os

FOLDER = '/home/markus/agenti-fsa/sara'

sys.path.insert( 0, FOLDER )
#import _thread
from SimpleWebSocketServer import SimpleSSLWebSocketServer
from chatterbot import ChatBot
from server import NLPController #, app as application

server = SimpleSSLWebSocketServer('localhost', 8020, NLPController, '/home/markus/agenti-fsa/sara/keys/fullchain.pem', '/home/markus/agenti-fsa/sara/keys/privkey.pem')
server.serveforever()

#_thread.start_new_thread( server.serveforever, () )

