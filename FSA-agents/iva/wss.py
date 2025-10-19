import sys, os

FOLDER = '/home/markus/agenti-fsa/iva'

sys.path.insert( 0, FOLDER )
#import _thread
from SimpleWebSocketServer import SimpleSSLWebSocketServer
from chatterbot import ChatBot
from server import NLPController #, app as application

iva = SimpleSSLWebSocketServer('localhost', 8013, NLPController, '/home/markus/agenti-fsa/iva/keys/fullchain.pem', '/home/markus/agenti-fsa/iva/keys/privkey.pem')
iva.serveforever()

#_thread.start_new_thread( iva.serveforever, () )

