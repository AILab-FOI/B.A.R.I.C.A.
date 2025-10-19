import sys, os

FOLDER = '/home/markus/agenti-fsa/drslavica'

sys.path.insert( 0, FOLDER )
#import _thread
from SimpleWebSocketServer import SimpleSSLWebSocketServer
from chatterbot import ChatBot
from server import NLPController #, app as application

drslavica = SimpleSSLWebSocketServer('localhost', 8012, NLPController, '/home/markus/agenti-fsa/drslavica/keys/fullchain.pem', '/home/markus/agenti-fsa/drslavica/keys/privkey.pem')
drslavica.serveforever()

#_thread.start_new_thread( drslavica.serveforever, () )

