#!/usr/bin/env python3

import json
from tqdm import tqdm
import os
import sys
import subprocess
import pty


import socket, errno
import threading
from time import sleep

DEBUG = False

# Used ports for streams
STREAM_PORTS = []

# Port manager thread stop flag
PORT_MANAGER_STOP = 0

#semaphore
threadLock = threading.Lock()

# STREAM_PORT manager in particular thread
class StreamPortManager(threading.Thread):
    def __init__(self, ip, timeDelay):
        threading.Thread.__init__(self)
        self.ip = ip
        self.timeDelay = timeDelay #number of cycles between port processing
        self.timeCount = timeDelay #cycle counter
        print("Port manager started")

    def run(self):
        global PORT_MANAGER_STOP
        while 1:
            if PORT_MANAGER_STOP == 1:
                break
            if(self.timeCount == self.timeDelay):
                self.portProcessing()
                self.timeCount = 0
            else:
                self.timeCount +=1
            sleep(0.5) # one cycle is 500 ms (0.5 s)
        
    def stop(self):
        global PORT_MANAGER_STOP
        PORT_MANAGER_STOP = 1
        print("Port manager stopping. Please wait for thread to exit.")
        

    def portProcessing(self):
        global STREAM_PORTS
        threadLock.acquire()
        print("Port processing...\n used ports: {0:d}".format(len(STREAM_PORTS)))
        for i in range(0,len(STREAM_PORTS)):
            if i < 0 or i >= len(STREAM_PORTS):
                threadLock.release()
                return
            p = STREAM_PORTS[i]
            if check_port(self.ip, p) == 1:
                print("IP: {0}, port {1:d} {2:s}".format(self.ip, p, "CLOSED"))
                del STREAM_PORTS[i]
                i -= 1
            else:
                print("IP: {0}, port {1:d} {2:s}".format(self.ip, p, "OPEN"))
        threadLock.release()


def get_stream_port(ip):
    global STREAM_PORTS
    result = -1
    threadLock.acquire()
    for i in range(2000,3000):
        if i in STREAM_PORTS:
            continue
        if check_port(ip,i) == 1:
            STREAM_PORTS.append(i)
            result = i
            break
    threadLock.release()
    print("Free port found: {0:d}".format(result))
    return result

def check_port(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.bind((ip,port))
    except socket.error as e:
        return 0
    finally:        
        s.close()
    return 1   



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
    def __init__( self, name, descriptor, location, ip):
        self.name = name
        self.descriptor = descriptor
        self.location = location
        self.ip = ip

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
                #port = get_stream_port()
                port = get_stream_port(self.ip)
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
            
def load_modules(ip):
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
                newmod = Module( mod[ "name" ], mod, dir_path, ip)
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
    load_modules('localhost')
