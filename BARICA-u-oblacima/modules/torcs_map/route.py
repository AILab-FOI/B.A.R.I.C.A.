#!/usr/bin/env python3

from pyxf.pyxf import flora2, Flora2QueryError
import json
import sys
import os

def route( frm, to, filters ):
    fl = flora2()
    print("Flora created")
    fl.load( os.path.join( os.path.dirname( __file__ ), "map") )
    print("Flora loaded")
    try:
        fl.query( 'newmodule{ pref }' )
    except Flora2QueryError:
        return None
    try:
        filters = [ i.split( '=' ) for i in filters ]
        filters = [ "p(%s,%s)" % ( i, j ) for i, j in filters ]
        filters = ','.join( filters )
        filters = '[%s]' % filters
        query = " %%preference_path( %s, %s, %s, ?path )."
        result = fl.query( query % ( frm, to, filters ) )
        return json.dumps( { "result":result } )
    except Flora2QueryError:
        return None
        

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument( "method", type=str, help="Specify the method to be run." )
    parser.add_argument( "arguments", nargs="*", help="Specify the arguments to be passed to the method" )
    args = parser.parse_args()

    if args.method == 'route':
        frm = args.arguments[ 0 ]
        to = args.arguments[ 1 ]
        filters = args.arguments[ 2: ]
        print( route( frm, to, filters ) )
