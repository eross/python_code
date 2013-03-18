import threading

a_lock = threading.Lock()
b_lock = threading.Lock()

a = 0
b = 100

def t1func():
    global a,b
    for i in xrange(1000):
        with a_lock:
            print "doing some A stuff"
            a = a + 2
            with b_lock:
                print "doing some B stuff"


def t2func():
    global a,b
    for i in xrange(1000):
        with b_lock:
            print b
            with a_lock:
                print a

t1 = threading.Thread(target = t1func)
t1.start()


t2 = threading.Thread(target = t2func)
t2.start()
