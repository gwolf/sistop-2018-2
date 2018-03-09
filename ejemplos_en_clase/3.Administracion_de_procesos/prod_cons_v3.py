#!/usr/bin/python
# *-* coding: utf-8
#
# Este archivo presenta una implementación del problema de
# "Productores y Consumidores" presentado en el libro
# (http://sistop.org/codigo/prod_cons_v2_py.html), modificándolo para
# que el tiempo empleado por la generación de un evento sea menor al
# que requiere su procesamiento (⅓ y ⅔ respectivamente del tiempo
# total). Si no ponemos un límite al buffer, éste crecerá
# indefinidamente. En esta versión, especificamos un buffer de
# longitud fija (definida por max_buffer).
#
# En clase mostramos que _parecía_ operar correctamente, pero había
# _alguna condición de carrera_ que hacía que después de algunas veces
# "cachar" correctamente que el buffer llegaba al límite, seguía
# incrementando.
#
# Esta versión lo corrige de forma bastante "puerca": En la línea 44,
# reemplacé "en_buffer == max_buffer" por un "en_buffer >=
# max_buffer". Como resultado, a veces llego a tener _seis_ elementos
# en el buffer.
#
# Puntos para quien lo arregle _bien_: Quien encuentre cómo hacer que
# funcione dejando esa compraración en igualdad estricta, y
# asegurándose de que no rebase _NUNCA_ a max_buffer.
#
# ¿Puedes resolverlo antes de vacaciones de Semana Santa? Si sí,
# cuenta de forma equivalent a un 10 en una práctica adicional para el
# primero que lo entregue (el primer pull request abierto), y como un
# 8 para los siguientes 3.
import threading
import time
import random
mutex = threading.Semaphore(1)  # Para proteger a buffer
mutex2 = threading.Semaphore(1) # Para proteger a en_buffer
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
        # mutex2 puede liberarse en ambas "ramas" del condicional. Es
        # feo, aunque seguro. ¡Evite hacerlo en codigo "real"!
        if en_buffer >= max_buffer:
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
            print "* * El buffer estaba lleno (%d). Lo libero." % en_buffer
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
