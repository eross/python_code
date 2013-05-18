__author__ = 'ericr'
a = [1,3, 5]
print type(a)

s = set(a)
s.add(15)
s.add(15)

t = list(s)

print s
print t