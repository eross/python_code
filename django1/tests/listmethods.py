import sys
import xmlrpclib
rpc_srv = xmlrpclib.ServerProxy("http://localhost:8000/rpc/")
result = rpc_srv.system.listMethods()
print result
print rpc_srv.system.methodHelp('multiply')
print rpc_srv.system.methodSignature('multiply')