#!/usr/bin/python
import subprocess
import sys
print "starting"
print "Main Python Interpretor",sys.executable
a = 42 + 55
print a
subprocess.call(['/usr/bin/python','./sub.py'])
print a+a

