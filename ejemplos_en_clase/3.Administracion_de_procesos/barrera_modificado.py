#!/usr/bin/python
# *-* coding: utf-8
#
# En este archivo tenemos una implementación de barrera derivada de la
# que presenta patron_barrera.py, modificada para volver a cerrar la
# barrera después de dejar pasar a los n hilos.
#
# Presenta aún un problema lógico: Funciona mientras se mantiene el
# flujo de hilos, pero al final se queda colgada porque necesariamente
# se queda esperando a barrera.acquire() cuando hilos==0.
#
# ¿Puedes resolverlo antes de vacaciones de Semana Santa? Si sí,
# cuenta de forma equivalente a un 10 en una práctica adicional para
# el primero que lo entregue (el primer pull request abierto), y como
# un 8 para los siguientes 3.
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
