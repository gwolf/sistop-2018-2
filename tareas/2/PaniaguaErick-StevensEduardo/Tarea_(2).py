from threading import Semaphore, Thread
from random import random
from time import sleep
from time import time 

num_hilos = 6
cont = 0
mutex = Semaphore (1)
torniquete = Semaphore(0)
conexion = Semaphore (10)


def jefe(id, torniquete):
    global cont, mutex
    print("\n Recibiendo solicitudes de conexión de red %d \n" % cont)
    sleep(random())
    mutex.acquire()
    cont = cont+1
    if cont != num_hilos:
               torniquete.release()
               print(" Se atenderán %d solicitudes!" % cont)
                         
    elif cont == 0:
                prnt(" No se tienen solicitudes... esperando solicitudes")
                torniquete.acquire()
                torniquete.release()
                print("Procesando solicitud número %d" % id)

def Conexion_red(id, conexion):
     conexion.acquire()
     print("Se están enviando %d conexiones de red\n" % id)
     time.sleep(random.random())
     conexion.release()
     print ("Terminando de enviar la conexión %d" % id)

for conexion_ in range (10):
    Thread(target = jefe, args = [conexion, mutex]).start()
