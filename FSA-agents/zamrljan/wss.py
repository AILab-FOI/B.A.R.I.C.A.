import sys, os

FOLDER = '/home/markus/agenti-fsa/zamrljan'

sys.path.insert( 0, FOLDER )
#import _thread
from SimpleWebSocketServer import SimpleSSLWebSocketServer
from chatterbot import ChatBot
from server import NLPController #, app as application

server = SimpleSSLWebSocketServer('localhost', 8011, NLPController, '/home/markus/agenti-fsa/zamrljan/keys/fullchain.pem', '/home/markus/agenti-fsa/zamrljan/keys/privkey.pem')
server.serveforever()

#_thread.start_new_thread( server.serveforever, () )

