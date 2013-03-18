__author__ = 'ericr'

import threading
import datetime
import time

class ThreadClass(threading.Thread):
    def run(self):
        time.sleep(10)
        now = datetime.datetime.now()
        print "%s says Hello World at time: %s" % (self.getName(), now)

for i in range(2):
    t = ThreadClass()
    t.start()



