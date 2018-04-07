# *-* encoding: utf-8 *-*
import threading
import time
import commands
import os


semaforo = threading.Semaphore(0) 

def mosSistema():
	import platform
	os.system("cls")
	print 'Descripción :', platform.uname()
	print 'Sistema :', platform.system()
	print "\n\n\nPresione ctl c para regresar al menu\n"
	time.sleep(40)
	semaforo.release() 
	return 0


def mosInfogral():
	os.system("cls")
	
	print "Informacion del sistema ", os.system("systeminfo")
	print "\n\n\nPresione control c para regresar al menu\n"
	time.sleep(40)
	semaforo.release() #Libera al hilo opcion para regresar al hilo menu
	return 0



def mosProcesador():
	import platform
	os.system("cls")
	
	print 'Tipo de Procesador :', platform.processor()
	print "\n\n\nPresione ctrl c para regresar al menu\n"
	time.sleep(40)
	semaforo.release() #Libera al hilo opcion para regresar al hilo menu
	return 0


#Menu de las opciones disponibles a ver.
def Menu():	
	global semaforo
	opcion = '0'
	while opcion != '4':
		os.system("cls")
		opciones = {'1':mosSistema,'2':mosInfogral,'3':mosProcesador}
		print "\t________________________________________________________"
		print "\t|	       Bienvenido a su Monitor de Sistema	 |"
		print "\t|_______________________________________________________|"
		
		print "Presione la opcion que desee saber. \n\n"
		print "1.- Descripcion y Version del Sistema.\n"
		print "2.- Informacion detallada del sistema.\n"
		print "3.- Modelo y caracteristicas del procesador.\n"
		print "4.- Salir.\n"
		print "\n\nDespues de 40 segundos de mostrar la opcion, el sistema regresa automaticamente al menu\n"		
		opcion = raw_input('\nSelecciona una opción: \n')		
		try:
			resultado = opciones[opcion]()
			semaforo.acquire() 
		except:
			if opcion != '4':
				print("Opción invalida")
Menu()