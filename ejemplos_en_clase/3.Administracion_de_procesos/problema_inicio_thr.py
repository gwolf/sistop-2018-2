#!/usr/bin/python
import threading
from time import sleep

class EjemploHilos:
    def __init__(self):
        self.x = 0

    def run(self):
        t1 = threading.Thread(target=self.f2, args=[])
        t2 = threading.Thread(target=self.f1, args=[t1])
        t1.start()
        t2.start()
        sleep(0.1)
        t2.join()
        print ' %d ' % self.x

    def f1(self, t):
        sleep(0.1)
        t.join()
        print '+',
        self.x += 3

    def f2(self):
        sleep(0.1)
        print '*',
        self.x *= 2

e = EjemploHilos()
for i in range(10):
    e.run()
