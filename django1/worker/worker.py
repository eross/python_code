import time
import os
import sys
from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
import xmlrpclib
import urlparse

import threading
RPCPATH='/rpc/'
# restrict to path
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = (RPCPATH,)

th = None
server = None
shutdown_event = threading.Event()

def shutdown():
    global th, server
    if th != None:
        th.stopsession()
        while th.isAlive():
            time.sleep(0.1)

        return 1
    print "shutting down server"
    shutdown_event.set()
    return 0

def send():
    global th
    pass

def receive():
    global th
    pass

def shutdownThread(evt):
    global server
    while not evt.isSet():
        time.sleep(0.4)
    server.shutdown()

# usage:  worker name callback_url
def main():
    global th, server, shutdown_event
    funcs = [shutdown, send, receive]
    for i in sys.argv:
        print i
    if len(sys.argv) != 3:
        print "Usage:  %s name url" % sys.argv[0]
        sys.exit(-1)
    os.setpgrp()
    pid = os.getpid()
    threading.Thread(target=shutdownThread,args=(shutdown_event,)).start()
    server = SimpleXMLRPCServer(('localhost',0),requestHandler=RequestHandler)
    for fcn in funcs:
        server.register_function(fcn)
    addr = server.server_address
    myurl = 'http://'+addr[0]+':'+str(addr[1])+RPCPATH
    rpc_srv = xmlrpclib.ServerProxy(sys.argv[2])
    rpc_srv.register(sys.argv[1],myurl)
    print server.server_address

    server.serve_forever(poll_interval=0.5)



if __name__ == '__main__':main()
