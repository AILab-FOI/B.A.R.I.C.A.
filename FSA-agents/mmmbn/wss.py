import sys, os

FOLDER = '/home/markus/agenti-fsa/mmmbn'

sys.path.insert( 0, FOLDER )
#import _thread
from SimpleWebSocketServer import SimpleSSLWebSocketServer
from chatterbot import ChatBot
from server import NLPController #, app as application

server = SimpleSSLWebSocketServer('localhost', 8016, NLPController, '/home/markus/agenti-fsa/mmmbn/keys/fullchain.pem', '/home/markus/agenti-fsa/mmmbn/keys/privkey.pem')
server.serveforever()

#_thread.start_new_thread( server.serveforever, () )

