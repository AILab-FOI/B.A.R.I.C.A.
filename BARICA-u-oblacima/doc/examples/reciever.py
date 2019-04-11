#!/usr/bin/python3 -u

import fileinput
import json
import urllib
from urllib.parse import quote
from urllib.request import urlopen
import subprocess
import sys

# Host and port of reciever
HOST = 'localhost'
PORT = 1234

# Query to B.A.R.I.C.A.
query = '''
{
    "module":"DummyStreamModule",
    "method":"fibonacci_stream",
    "args":[ "%s", %d ]
}
''' % ( HOST, PORT )

# Connect to B.A.R.I.C.A. to get the
# port she is listening to
def connect( host, port ):
    q = "http://%s:%d/ask/%s" % ( host, port, quote( query ) )
    result = urlopen( q )
    result = json.load( result )
    return result[ "port" ]
 
# Use with netcat, e.g.
# nc -lp 1234 | ./reciever.py localhost 5000
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument( "host", type=str, help="B.A.R.I.C.A. host." )
    parser.add_argument( "port", type=int, help="B.A.R.I.C.A. port." )
    parser.add_argument( "num", type=int, help="Number of Fibonacci numbers to be processed.", default=100, nargs='?' )
    args = parser.parse_args()


    port = connect( args.host, args.port )

    # Start a random number generator program
    # (can be anything)
    command = [ "./num-generator.sh", str( args.num ), "|", "nc", args.host, str( port ) ]
    proc = subprocess.Popen( ' '.join( command ), shell=True )

    # Now listen to standard input and
    # process the incomming numbers
    for line in fileinput.input( '-' ):
        if line.startswith( "Sorry" ):
            print( "0000" )
        else:
            print( line[ :-1 ] )
        if ord( line[ 0 ] ) == 10:
            sys.exit()
