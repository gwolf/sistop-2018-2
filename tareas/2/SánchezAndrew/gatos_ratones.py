import threading
import time
import random

senalGato = threading.Semaphore(0)
senalRaton = threading.Semaphore(0)
senalPlato = threading.Semaphore(0)
senalComeRaton = threading.Semaphore(0)

mutexPlato = threading.Semaphore(1) 

global platos, gatos, ratones
platos = []
gatos = []
ratones = []
global indexp, indexg, indexr
indexp = 0
indexg = 0
indexr = 0

class Comer:
	global platos, gatos, ratones, indexr, indexp, indexg

	def gato_come(self):
		print "gato comiendo"

	def raton_come(self):
		print "raton comiendo"

	def gato_raton(self):
		print "que rico raton"



def Plato():
	global platos, indexp
	while True:

		mutexPlato.acquire()
		indexp += 1
		print "hay %d plato" % indexp
		platos.append(indexp)
		mutexPlato.release()

		senalPlato.release()
		senalGato.release()
		senalRaton.release()
		


def Gato():
	global gatos, ratones, indexg, indexr
	while True:
		comeg = Comer()

		senalPlato.acquire()
		indexg += 1
		print "hay %d gato" %indexg
		gatos.append(indexg)

		senalRaton.acquire()
		comeg.gato_come()

		senalComeRaton.acquire()
		comeg.gato_raton()
		ratones.pop()
		indexr -= 1



def Raton():
	global ratones, indexr
	while  True:
		comeR = Comer()

		senalPlato.acquire()
		senalGato.acquire()
		indexr += 1
		print "hay %d raton" % indexr
		ratones.append(indexr)

		senalRaton.release()	
		comeR.raton_come()
		senalComeRaton.release()

		

threading.Thread(target = Plato, args = []).start()
threading.Thread(target = Gato, args = []).start()
threading.Thread(target = Raton, args = []).start()