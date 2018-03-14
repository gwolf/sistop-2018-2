#!/usr/bin/python
import threading
from time import sleep

class EjemploHilos:
    def __init__(self):
        self.x = 0
        self.s1 = threading.Semaphore(0)
        self.s2 = threading.Semaphore(0)

    def run(self):
        t1 = threading.Thread(target=self.f2, args=[])
        t2 = threading.Thread(target=self.f1, args=[])
        t1.start()
        t2.start()
        sleep(0.1)
        self.s1.acquire()
        print ' %d ' % self.x

    def f1(self):
        sleep(0.1)
        print '+',
        self.x += 3
        self.s2.release()

    def f2(self):
        sleep(0.1)
        self.s2.acquire()
        print '*',
        self.x *= 2
        self.s1.release()

e = EjemploHilos()
for i in range(10):
    e.run()
