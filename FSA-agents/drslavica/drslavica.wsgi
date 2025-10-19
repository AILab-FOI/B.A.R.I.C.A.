'''
try:
        import sys, os

        FOLDER = '/home/markus/agenti-fsa/drslavica'

        sys.path.insert( 0, FOLDER )
        import _thread
        from SimpleWebSocketServer import SimpleSSLWebSocketServer
        from chatterbot import ChatBot
        from server import NLPController, app as application
except Exception as e:
        fl = open( '/tmp/drslavica.log', 'w' )          
        fl.write( str( e ) )
        fl.close()

'''

import sys, os

FOLDER = '/home/markus/agenti-fsa/drslavica'

sys.path.insert( 0, FOLDER )
import _thread
from SimpleWebSocketServer import SimpleSSLWebSocketServer
from chatterbot import ChatBot
from server import NLPController, app as application

#drslavica = SimpleSSLWebSocketServer('localhost', 8009, NLPController, '/home/markus/agenti-fsa/drslavica/keys/fullchain.pem', '/home/markus/agenti-fsa/drslavica/keys/privkey.pem')

#_thread.start_new_thread( drslavica.serveforever, () )
