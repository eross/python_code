__author__ = 'ericr'

import xmlrpclib
import random
import string
import StringIO
import sys

def printAPI(server):
    for method in server.system.listMethods():
        print method
        print '\n'.join(['  ' + x for x in server.system.methodHelp(method).split('\n')])

def randomString():
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(6))

server = xmlrpclib.ServerProxy("https://eric.ross@hp.com:X@sal.vcd.hp.com/sandbox/login/xmlrpc")
#printAPI(server)

results = server.ticket.query("status!=closed")

attributes = {'status':'closed','resolution':'wontfix'}
for tick in results:
    print server.ticket.get(tick)

#    server.ticket.update(tick,"Auto Closed Ticket",attributes)

sys.exit(0)


attributes = {'status':'new','reporter':'eric.ross@hp.com','component':'component1'}
#ticket = server.ticket.create("This is an automated ticket -- "+randomString(),"This is a ticket created by an automated system",attributes)
changes = {'description': "This is a ticket created by an automated system",'type':'testrun','owner':'alva.barney@hp.com'}
tick = server.ticket.get(3)
#print server.ticket.update(3,"Updated ticket",changes)

#with open('comment.txt') as f:
#    comment = f.read()

buf = StringIO.StringIO()

buf.write("Multiples of PI (approx)\n")
for i in range(10):
    buf.write(str(i)+", "+str(i*3.14159)+"\n")


server.ticket.update(3,buf.getvalue())
buf.close()


#print "Ticket id: ",ticket," created"

#print server.ticket.getActions(3)