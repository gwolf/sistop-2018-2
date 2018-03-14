#!/usr/bin/python
# -*- encoding: utf-8
from threading import Semaphore, Thread
from random import random
from time import sleep
# Por convención, el piso mínimo SIEMPRE debe ser cero.
global piso_min, piso_max
piso_min = 0
piso_max = 5

class Elevador:
    def __init__(self):
        global piso_max, piso_min
        self.max_pers = 5
        self.piso_max = piso_max
        self.piso_min = piso_min
        self.piso_actual = self.piso_min
        self.mutex_colas = Semaphore(1)
        self.colas = [ [] for piso in range(self.piso_min, self.piso_max) ]
        self.pasajeros = []
        self.mutex_pasajeros = Semaphore(1)

    def aborda(self, persona):
        pass # A trabajar...

    def ve_a(self, piso):
        if piso < self.piso_min or piso > self.piso_max:
            print "No me pidas imposibles (%d <= %d <= %d)" % (self.piso_min, piso, self.piso_max)
            return 1

        while piso != self.piso_actual:
            print "Moviéndome... %d" % self.piso_actual
            if piso > self.piso_actual:
                sleep(0.3)
                self.piso_actual += 1
            else:
                sleep(0.2)
                self.piso_actual -= 1

        print "Ya llegué al piso %d" % piso
        return 0

    def llama(self,piso, persona):
        self.mutex_colas.acquire()
        self.colas[piso].append(persona)
        self.mutex_colas.release()

        self.ve_a(piso)

        self.mutex_pasajeros.acquire()
        self.mutex_colas.acquire()
        while len(self.pasajeros) < self.max_pers and len(self.colas[piso]) > 0:
            persona = self.colas[piso][0]
            self.colas[piso] = self.colas[piso][1:]
        self.mutex_colas.release()
        self.mutex_pasajeros.release()

class Persona:
    def __init__(self, elev):
        global piso_min, piso_max
        mi_piso = int(random() * len(range(piso_min, piso_max)))
        piso_dest = int(random() * len(range(piso_min, piso_max)))
        if mi_piso == piso_dest:
            print "¡Viva! ¡Viva! ¡No necesito formarme!"
        print "Llamando al elevador (piso %d)" % mi_piso
        e.llama(mi_piso, self)
        print "Estoy en el elevador. Voy del %d al %d" % (mi_piso, piso_dest)
        e.ve_a(piso_dest)
        print "Llegué a mi destino, %d" % piso_dest

e = Elevador()
while True:
    print "Generando a una persona..."
    sleep(random())
    p = Thread(target=Persona, args=[e])
    p.start()
