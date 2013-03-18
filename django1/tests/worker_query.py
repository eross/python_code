import sys
import xmlrpclib
rpc_srv = xmlrpclib.ServerProxy("http://localhost:60184/rpc/")
rpc_srv.shutdown()
