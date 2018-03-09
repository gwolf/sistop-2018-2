#!/usr/bin/python
# *-* coding: utf-8
from threading import Semaphore, Thread
from random import random
from time import sleep
num_hilos = 5
cuenta = 0
mutex = Semaphore(1)
barrera = Semaphore(1)

def vamos(id):
    global cuenta, mutex, barrera
    print "Inicializando al hilo %d" % id
    sleep(random())
    mutex.acquire()
    cuenta = cuenta + 1
    if cuenta == 0:
        barrera.acquire()
    elif cuenta == num_hilos:
        print "Tengo %d hilos. ¡Se abre la barrera!" % cuenta
        cuenta = 0
        barrera.release()
    mutex.release()
    print "... ¿Esperaremos a la barrera?"
    barrera.acquire()
    barrera.release()
    print "Procesando al hilo %d" % id

for i in range(10):
    Thread(target=vamos, args=[i]).start()
