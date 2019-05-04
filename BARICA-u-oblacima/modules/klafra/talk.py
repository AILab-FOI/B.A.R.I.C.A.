#!/usr/bin/env python3

import json
from chatterbot import ChatBot
import os

dbpath = os.path.join( os.path.dirname( os.path.abspath( os.path.realpath( __file__ ) ) ), 'db.sqlite3' )

chatbot = ChatBot(
    'BARICA_SLACK',
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    database_uri="sqlite:///"+dbpath
)

def answer( msg ):
    return str( chatbot.get_response( msg ) ) 

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument( "method", type=str, help="Specify the method to be run." )
    parser.add_argument( "arguments", nargs="*", help="Specify the arguments to be passed to the method" )
    args = parser.parse_args()

    if args.method == 'answer':
        msg = " ".join( args.arguments[ 0: ] )
        if msg == "Bok":
            print( json.dumps( { "result":"Bok" } ) )
        else:
            print( json.dumps( { "result":answer( msg ) } ) )
