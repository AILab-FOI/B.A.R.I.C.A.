#!/usr/bin/env python3

import json
from tqdm import tqdm
import os
import sys
import subprocess
import pty
from time import sleep

DEBUG = False

# Used ports for streams
STREAM_PORTS = []

def get_stream_port():
    ''' TODO: make ports rotate, now it will
        go from 2000 until forever. '''
    global STREAM_PORTS
    if STREAM_PORTS:
        port = STREAM_PORTS[ -1 ] + 1
    else:
        port = 2000
    STREAM_PORTS.append( port )
    return port


# Stolen from https://stackoverflow.com/questions/229186/os-walk-without-digging-into-directories-below
def walklevel( some_dir, level=1 ):
    some_dir = some_dir.rstrip( os.path.sep )
    assert os.path.isdir( some_dir )
    num_sep = some_dir.count( os.path.sep )
    for root, dirs, files in os.walk( some_dir ):
        yield root, dirs, files
        num_sep_this = root.count( os.path.sep )
        if num_sep + level <= num_sep_this:
            del dirs[ : ]

# Exception to be thrown if there is
# an error while running the module
class ModuleException( Exception ):
    pass
            
# Module class
class Module:
    def __init__( self, name, descriptor, location ):
        self.name = name
        self.descriptor = descriptor
        self.location = location

    def __str__( self ):
        return json.dumps( self.descriptor, indent=4, sort_keys=True )
        
    def run( self, method, args ):
        '''
        Check if the method's input is:
        (a1) command line arguments
        (b1) stdin
        Check if the method's output is:
        (a2) stdout (json) - one shot
        (b2) stdout (any format) - stream
        '''
        if self.descriptor[ "methods" ][ method ][ "stdin_stream" ]:
            if self.descriptor[ "methods" ][ method ][ "stdout_stream" ]:
                port = get_stream_port()
                command = [ "nc", "-lp", str( port ), "|", os.path.join( self.location, self.descriptor[ "methods" ][ method ][ "run" ] ), method, "|", "nc", args[ 0 ], str( args[ 1 ] ) ]
                try:
                    proc = subprocess.Popen( ' '.join( command ), shell=True )
                    return '''{ "port":%d }''' % port
                except Exception as e:
                    raise ModuleException( "Error while running module %s. Error was:\n%s" % ( self.name, str( e ) ) )
            else:
                raise NotImplemented( "Error: Currently module methods can only get and respond with streams or arguments exclusively, not combined!" )
        else:
            if self.descriptor[ "methods" ][ method ][ "stdout_stream" ]:
                raise NotImplemented( "Error: Currently module methods can only get and respond with streams or arguments exclusively, not combined!" )
            else:
                try:
                    return subprocess.check_output( [ os.path.join( self.location, self.descriptor[ "methods" ][ method ][ "run" ] ), method ] + args )
                except Exception as e:
                    raise ModuleException( "Error while running module %s. Error was:\n%s" % ( self.name, str( e ) ) )
            
def load_modules():
    bar = tqdm( walklevel( 'modules', level=1 ) )
    modules = {}
    
    def printt( smth ):
        bar.set_description( str( smth ) )
        if DEBUG:
            sleep( 1 )

    for dir_path, subdir_list, file_list in bar:
        for fname in file_list:
            full_path = os.path.join( dir_path, fname )
            if fname == 'interface.json':
                mod = json.loads( open( full_path ).read() )
                printt( "Processing %s" % mod[ 'name' ] )
                newmod = Module( mod[ "name" ], mod, dir_path )
                modules[ mod[ 'name' ] ] = newmod
                for m in mod[ "methods" ]:
                    method = mod[ "methods" ][ m ]
                    printt( "Processing method %s" % m )
                    if method[ "stdin_stream" ]:
                        master, slave = pty.openpty()
                        command = [ os.path.join( dir_path, method[ "run" ] ), m ]
                        proc = subprocess.Popen( ' '.join( command ), stdin=subprocess.PIPE, shell=True, stdout=slave )
                        stdin_handle = proc.stdin
                        stdout_handle = os.fdopen( master )
                        result = ''
                        for line in method[ "testcase" ][ "input" ]:
                            stdin_handle.write( ( line + '\n' ).encode( 'utf-8' ) )
                            stdin_handle.flush()
                            result += stdout_handle.readline()
                    else:
                        result = subprocess.check_output( [ os.path.join( dir_path, method[ "run" ] ), m ] + method[ "testcase" ][ "input" ] )
                        result = json.loads( result )[ "result" ]
                    if str( result ) == method[ "testcase" ][ "output" ]:
                        printt( "Method %s tested succesfully!" % m )
                    else:
                        raise ModuleException( 'Error while testing method "%s" in module "%s"!\nExpected output:\n$%s$\nGot:\n$%s$' % ( m, newmod.name, method[ "testcase" ][ "output" ], str( result ) ) )
                if DEBUG:
                    print( newmod )
    return modules



if __name__ == '__main__':
    load_modules()
