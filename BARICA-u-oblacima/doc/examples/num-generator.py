#!/usr/bin/python3 -u

from random import randint

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument( "howmuch", type=int, help="Specify the number of integers to be generated." )
    args = parser.parse_args()
    for i in range( args.howmuch ):
        print( randint( 1, 35 ) )
    print( '\\x' )
