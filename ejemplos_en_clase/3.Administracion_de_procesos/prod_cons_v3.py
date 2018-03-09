import threading
import time
import random
mutex = threading.Semaphore(1)
mutex2 = threading.Semaphore(1)
elementos = threading.Semaphore(0)
buffer = []
en_buffer = 0
max_buffer = 5
buffer_lleno = threading.Semaphore(0)

class Evento:
    def __init__(self):
        self.ident = random.random()
        print "Generando evento %1.3f" % self.ident
        time.sleep(self.ident * 1/3)
    def process(self):
        print "Procesando evento %1.3f" % self.ident
        time.sleep(self.ident * 2/3)

def productor():
    global en_buffer
    while True:
        event = Evento()
        mutex2.acquire()
        if en_buffer == max_buffer:
            mutex2.release()
            print "*** Tengo el buffer lleno (%d)" % en_buffer
            buffer_lleno.acquire()
        else:
            mutex2.release()
            print " *  Buffer con espacio (%d)" % en_buffer
        mutex.acquire()
        en_buffer += 1
        buffer.append(event)
        mutex.release()
        elementos.release()

def consumidor():
    global en_buffer
    while True:
        elementos.acquire()
        mutex2.acquire()
        if en_buffer == max_buffer:
            print "* * El buffer estaba lleno (%d). Lo libero."
            buffer_lleno.release()
        mutex2.release()
        mutex.acquire()
        en_buffer -= 1
        event = buffer.pop()
        print "Quedan %d elementos en el buffer" % en_buffer
        mutex.release()
        event.process()

threading.Thread(target=productor, args=[]).start()
threading.Thread(target=consumidor, args=[]).start()
