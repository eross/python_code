__author__ = 'ericr'

import xmlrpclib
import random
import string
import StringIO
import base64
import os

# Helper function
def genTestID():
    """
    Generate a 6 character random ID
    """
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(6))


# main
server = xmlrpclib.ServerProxy("https://eric.ross@hp.com:mWiavcc5.....@sal.vcd.hp.com/sandbox/login/xmlrpc")

attributes = {'status':'new','reporter':'eric.ross@hp.com','component':'component1','type':'testrun',
              'test_run':genTestID(),'test_passed':'no'}
description="Component 1 Test"

ticket = server.ticket.create(description,"Automated Test Run Data",attributes)

# Now simulate running the test.
buf = StringIO.StringIO()

buf.write("Some random numbers\n")
for i in range(10):
    buf.write(str(i)+", "+str(random.uniform(0,100))+"\n")

testresult = {'test_passed':'yes'}
server.ticket.update(ticket,buf.getvalue(),testresult)
buf.close()

# attach the image if it exists
for image in ['image.jpg','hplogo.jpg']:
    os.path.isfile(image)

    with open(image) as f:
        server.ticket.putAttachment(ticket,image,"Attached image",xmlrpclib.Binary(f.read()))

print "Test results saved in ticket: ",str(ticket)
