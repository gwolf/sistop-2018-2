from threading import Semaphore, Thread
from random import random
from time import sleep

global serfs
global hackers
global balsas
global pasajeros


def serf(hilo):
	global serfs
	global hackers
	self.mutex_cola = Semaphore(1)
	self.serfs_cola = Semaphore(0)
	self.hackers_cola = Semaphore(0)
	
	mutex_cola.acquire()
	serfs+=1
	if serfs == 4:
		pasa(serfs_cola,4)
		serfs-=4
		mutex_cola.release()
	elif serfs == 2 and hackers >=2:
		paso(hackers_cola,2)
		paso(serfs_cola,2)
		hackers -=2
		mutex_cola.release()
	else:
		mutex_cola.release()

	serfs_cola.acquire()

	if balsa.broken:
		boat.reset()
	boat.wait()
	lock.acquire()
	subir("serfs",hilo)
	lock.release()

def hacker(hilo):
	global serfs
	global hackers
	self.mutex_cola = Semaphore(1)
	self.serfs_cola = Semaphore(0)
	self.hackers_cola = Semaphore(0)
	self.lock = threading.Lock()
	mutex_cola.acquire()
	hackers+=1
	if hackers == 4:
		pasa(hackers_cola,4)
		hackers-=4
		mutex_cola.release()
	elif hackers == 2 and serfs >=2:
		paso(hackers_cola,2)
		paso(serfs_cola,2)
		hackers -=2
		serfs -=2
		mutex_cola.release()
	else:
		mutex_cola.release()

	hackers_cola.acquire()

	if balsa.broken:
		boat.reset()
	boat.wait()
	lock.acquire()
	subir("hackers",hilo)
	lock.release()
		


def balsa():
	global nuevabal

	nuevabal+=1
	time.sleep(0.3)
	print('Balsa ',nuevabal,' saliendo')


def subir(prog,hilo):
	global pasajeros

	pasajeros+=1
   	print ('Soy un '+prog+' mi numero es',hilo)
   	if pasajeros == 4:
   		balsa()
   		pasajeros=0

def paso(self,times):
   	for i in range(times):
       	serf.release():


while True:
    s = Thread(target=serf, args=[e])
    h = Thread(target=hacker, args=[e])
    s.start()
    h.start()