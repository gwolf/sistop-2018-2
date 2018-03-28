# *-* Encoding: utf-8
import threading #Importamos la biblioteca threading para usar hilos
def autorizar_balsa():
	global balsa	
	mutex.acquire()#Iniciamos nuestro MUTEX de protección para indicar el número de desarrolladores por bando
	if len(balsa)!=4:
		mutex.release() 
		semaforo_hacker.acquire()
		if len(hacker)!=0:
			balsa.append(hacker)
		else:
			semaforo_hacker.release()
		if len(balsa)!=4 :
			semaforo_serf.acquire()
			if len(serf)!=0:
				balsa.append(serf)
			else:
				semaforo_serf.release()
	else:	
		print ('\nOk, balanceo de desarrolladores justo :)\nEnviando balsa...\n\nBienvenidos:  ')		
		print (balsa)
		balsa=[]	
		semaforo_hacker.release()# Autoriza hackers
		semaforo_serf.release()#Autoriza serfs
		mutex.release()#Terminamos nuestro MUTEX de protección
balsa=[]
hacker=[]
serf=[]
mutex=threading.Semaphore(1)
semaforo_hacker=threading.Semaphore(2)
semaforo_serf=threading.Semaphore(2)
hilos=[]
hilo_serf     = int (input('\n¿Cuántos Serfs(Microsoft) abordarán la balsa?: '))
hilo_hacker = int (input('¿Cuántos Hackers(GNU-Linux) abordarán la balsa?: '))
#print ('Error, exceso de desarrolladores')
for i in range(hilo_serf):
	serf.append('Serf_Numero.'+str(i))
for i in range(hilo_hacker):
	hacker.append('Hacker_Numero.'+str(i))
for i in range(hilo_hacker):
	hilos.append(threading.Thread(target=autorizar_balsa))
for i in range(hilo_serf):
	hilos.append(threading.Thread(target=autorizar_balsa))
for i in range(hilo_serf+hilo_hacker):
	hilos[i].start()
