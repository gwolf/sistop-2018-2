#Monitor de Recursos 
#Berdejo Arvizu Oscar

from threading import Semaphore, Thread
import os, threading, time

semaforo = threading.Semaphore(1)
band = 0 #Esta es utilizada para activar el menu "eleccion" y y el el modulo de la opcion de salida lo cambia para terminar con el sistema

#Funciones que llaman a la biblioteca os para desplegar info
def procesos():
	global semaforo
	semaforo.acquire()
	print"--Procesos que hay en el sistema--"
	os.system("ps -auf")
	semaforo.release()

def usoDisco():
	global semaforo
	semaforo.acquire()
	print("--Espacio usado en el disco--")
	os.system("du -h")
	semaforo.release()

def procesosArbol():
	global semaforo
	semaforo.acquire()
	print("--Procesos en forma de arbol--")
	os.system("pstree")
	semaforo.release()

def logins():
	global semaforo
	semaforo.acquire()
	print("--Logins del Sistema--")
	os.system("last")
	semaforo.release()

def infoCPU():
	global semaforo
	semaforo.acquire()
	print("--Informacion del CPU--")
	os.system("cat /proc/cpuinfo")
	semaforo.release()

def interrupciones():
	global semaforo
	semaforo.acquire()
	print("--Interrupciones del CPU--")
	os.system("cat /proc/interrupts")

def usoMemoria():
	global semaforo
	semaforo.acquire()
	print("--Uso de Memorias--")
	os.system("free -h")
	os.system("cat /proc/meminfo")
	semaforo.release()

def limpiarPantalla():
	global semaforo
	semaforo.acquire()
	os.system("clear")
	semaforo.release()

def menu(var):
    #Asignacion de los hilos
    global band 
    if var == "Procesos":
        thr = threading.Thread(target = Procesos)
        thr.start()
    elif var == "Disco":
        thr = threading.Thread(target = usoDisco)
        thr.start()
    elif var == "Arbol":
        thr = threading.Thread(target = procesosArbol)
        thr.start()
    elif var == "Logins":
        thr = threading.Thread(target = logins)
        thr.start()
    elif var == "CPUInfo":
        thr = threading.Thread(target = infoCPU)
        thr.start()
    elif var == "Interrupciones":
        thr = threading.Thread(target = interrupciones)
        thr.start()
    elif var == "Memoria":
        thr = threading.Thread(target = usoMemoria)
        thr.start()
    elif var == "Limpiar":
        thr = threading.Thread(target = limpiarPantalla)
        thr.start()
    elif var == "Ayuda":
    	print("Procesos:Muestra los procesos abiertos en memoria con la informacion Uso del CPU, Uso de memoria, Estado, Comando, etc  ")
    	print("Disco: Cantidad de memoria utilizada en el disco")
    	print("Arbol: Muestra los procesos corriendo en forma de arbol, sin la informacion que otorga el comando *Procesos*")
    	print("Logins: Muestra Logins del Sistema")
    	print("cpuInfo: Imprime la informacion del CPU, arquitectura, procesadores, etc")
    	print("Interrupciones:")
    	print("Memoria: Informacion de las memorias que contiene la maquina, Buffers, RAM.")
    elif var == "Salir":
        print ""
        band = 1  

def hilo():
    thr0 = threading.Thread(target = Procesos)
    thr0.start()
    thr1 = threading.Thread(target = usoDisco)
    thr1.start()
    thr2 = threading.Thread(target = procesosArbol)
    thr2.start()
    thr3 = threading.Thread(target = logins)
    thr3.start()
    thr4 = threading.Thread(target = infoCPU)
    thr4.start()
    thr5 = threading.Thread(target = interrupciones)
    thr5.start()
    thr6 = threading.Thread(target = usoMemoria)

def eleccion():
	#Menu para seleccionar comandos
	global var, band, semaforo
	os.system("clear")
	while band == 0:
		time.sleep(.1)
		print("Comandos a Realizar")
		print("Procesos, Disco, Arbol, Logins, CPUInfo Interrupciones, Memoria, Limpiar, Ayuda, Salir")
		var = raw_input(":3$ ")
		menu(var)

eleccion()