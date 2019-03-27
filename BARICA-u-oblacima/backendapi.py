#!/usr/bin/env python3

import json
from tqdm import tqdm
import os
import subprocess
from time import sleep

DEBUG = False

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
                    result = subprocess.check_output( [ os.path.join( dir_path, method[ "run" ] ), m ] + method[ "testcase" ][ "input" ] )
                    result = json.loads( result )[ "result" ]
                    if str( result ) == method[ "testcase" ][ "output" ]:
                        printt( "Method %s tested succesfully!" % m )
                if DEBUG:
                    print( newmod )
    return modules



if __name__ == '__main__':
    load_modules()
