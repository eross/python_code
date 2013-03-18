#!python
'''Experiments with modules'''
import mod1


#import mod1.sub1
import xml


def printModInfo(mod):
	print "Module Info:  ",mod, dir(mod)
	print
	
def printDict(l):
	for i in l.keys():
		print i,": ",l[i]
print "locals()"		
printDict(locals())

print "\nglobals()"
printDict(globals())

print

printModInfo(__name__)	
#print "Running process: ",os.getpid()

printModInfo(mod1)
printModInfo(mod1.sub1)
#printModInfo(sub1)

printModInfo(xml)

print mod1.sub1.subfuncs.theAnswer()

