#!/usr/bin/python3 -u

import fileinput

END = '\\x'

def fibb( x ):
    if x > 30:
        print( 'Sorry, number has to be lower than 30!' )
        return 0
    if x == 1 or x == 2:
        return 1
    else:
        return fibb( x-1 ) + fibb( x-2 )


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument( "method", type=str, help="Specify the method to be run." )
    args = parser.parse_args()
    #print( args )
    if args.method == 'fibonacci_stream':
        for line in fileinput.input( '-' ):
            nums = [ j for j in line.rstrip().split() ]
            for i in nums:
                try:
                    i = int( i )
                    print( fibb( i ) )
                except:
                    if i == END:
                        print( '\n' )
                        break
                
