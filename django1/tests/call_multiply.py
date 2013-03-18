import sys
import xmlrpclib
rpc_srv = xmlrpclib.ServerProxy("http://localhost:8000/rpc/")
result = rpc_srv.multiply( int(sys.argv[1]), int(sys.argv[2]))
print "%s * %s = %d" % (sys.argv[1], sys.argv[2], result)