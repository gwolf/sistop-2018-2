"""
Proyecto 1 de sistemas operativos
Monitor de sistema 
INTEGRANTES : CORTES BENITEZ YAIR // FLORES GASPAR JUAN ANTONIO //
"""
from colorama import Fore, init, Style, Back, Cursor	#para cambiar de color y formato las impresiones en consola
import threading   										#para el manejo de hilos
import subprocess  										#para ejecutar comandos del sistema operativo o lanzar programas
import platform    										#para acceder a datos del sistema 
from time import sleep									#para esperar cierto tiempo
semaforo_total=threading.Semaphore(1)					#semaforo para manejar los hilos iniciados
borra=0													#contador de ayuda para borrar la pantalla una vez elegida alguna opcion

init()								

def borra_pantalla():#función para limpiar la consola
	subprocess.run("clear", shell=True)
"""
Sistema es una función que usando el módulo platform de python nos va a dar
información acerca de la maquina en donde se está ejecutando el programa
"""
def sistema():
	global semaforo_total
	semaforo_total.acquire()
	borra_pantalla()
	print(Cursor.DOWN(5)+Cursor.FORWARD(10)+Back.RED+Fore.WHITE+"================ INFORMACIÓN DE SISTEMA =================="+Style.RESET_ALL)
	print(Cursor.FORWARD(10)+Cursor.DOWN(2)+Fore.RED+"Sistema : ", platform.system())
	print(Cursor.FORWARD(10)+"Arquitectura de: ", platform.architecture())
	print(Cursor.FORWARD(10)+"Máquina: ", platform.machine())
	print(Cursor.FORWARD(10)+"Procesador: ", platform.processor())
	print(Cursor.FORWARD(10)+"Red", platform.node())
	print(Cursor.FORWARD(10)+"Versión de sistema operativo: ", platform.version())
	print(Cursor.FORWARD(10)+"Versión de Python: ", platform.python_version())
	sleep(5)
	semaforo_total.release()
	
"""
discos es una función que usando el módulo subprocess de python
va a ejecutar un comando (df -h) para que el sistema nos devuelva el nombre, la 
capacidad y el directorio en donde estan montados los discos de la 
computadora
"""	
def discos():
	global semaforo_total
	semaforo_total.acquire()
	borra_pantalla()
	print(Cursor.DOWN(5)+Cursor.FORWARD(5)+Back.GREEN+Fore.WHITE+"================= INFORMACIÓN DE DISCOS ==================\n\n"+Style.RESET_ALL+Fore.GREEN)
	subprocess.run(["df","-h"])
	sleep(5)
	semaforo_total.release()
	
"""
memoria es una función que usando el módulo subprocess de python
va a ejecutar el comando ( free -m )para que el sistema nos devuelva 
información acerca de la memoria RAM y también va a ejecutar el comando
(cat /proc/meminfo) para dar información más detallada de la memoria de
la computadora en donde estamos ejecutando el programa
"""	
def memoria():
	global semaforo_total
	semaforo_total.acquire()
	borra_pantalla()
	print(Cursor.DOWN(5)+Cursor.FORWARD(5)+Back.MAGENTA+Fore.WHITE+"================= INFORMACIÓN DE MEMORIA RAM ===============\n\n"+Style.RESET_ALL+Fore.MAGENTA)
	subprocess.run(["free", "-m"])
	sleep(5)
	borra_pantalla()
	print(Cursor.DOWN(5)+Cursor.FORWARD(5)+Back.MAGENTA+Fore.WHITE+"============ INFORMACIÓN GENERAL DE LA MEMORIA ==========\n\n"+Style.RESET_ALL+Fore.MAGENTA)
	subprocess.run(["cat", "/proc/meminfo"])
	sleep(5)
	semaforo_total.release()	
	
"""
mostrar_procesos_tiempo_real es una función en donde usando el módulo 
subprocess de python se va a ejecutar el comando (htop) para iniciar el
programa htop y poder ver información sobre los procesos que se están 
ejecutando en el sistema operativo
"""
def mostrar_procesos_tiempo_real():
	global semaforo_total
	semaforo_total.acquire()
	subprocess.run("htop", shell=True)
	semaforo_total.release()
	
"""
procesos es una función que usando el módulo subprocess de python se va
a ejecutar el comando (ps -e) para ver los procesos que se están ejecutando 
en la computadora.

ps -e devuelve información acerca de los procesos de la computadora
pero no se queda en ejecución como ocurre con htop.
Por ello esta función es la que se manda a llamar cuando se elige la 
opción de análisis general del sistema  
"""
def procesos():
	global semaforo_total
	semaforo_total.acquire()
	borra_pantalla()
	print(Cursor.DOWN(5)+Cursor.FORWARD(5)+Back.CYAN+Fore.WHITE+"=============== INFORMACIÓN DE PROCESOS ==========\n\n"+Style.RESET_ALL+Fore.CYAN)
	subprocess.run(["ps", "-e"])
	sleep(5)
	semaforo_total.release()
	
"""
cpu es una función que usando el módulo subprocess de python se va a 
ejecutar el comando (lscpu) que nos da información sobre la CPU de la 
computadora en donde estamos ejecutando el programa
"""	
def cpu():
	global semaforo_total
	semaforo_total.acquire()
	borra_pantalla()
	print(Cursor.DOWN(5)+Cursor.FORWARD(5)+Back.BLUE+Fore.WHITE+"============== INFORMACIÓN DE CPU ==========\n\n"+Style.RESET_ALL+Fore.BLUE)
	subprocess.run("lscpu", shell=True)
	sleep(5)
	semaforo_total.release()
	
"""
buses_puertos es una función que usando el módulo subprocess de python 
va a ejecutar el comando (lspci) que nos devuelve información sobre todos
los buses PCI de la computadora. También va a ejecutar el comando (lsusb)
que nos regresa información de los puertos USB de la computadora.
"""	
def buses_puertos():
	global semaforo_total
	semaforo_total.acquire()
	borra_pantalla()
	print(Cursor.DOWN(5)+Cursor.FORWARD(5)+Back.RED+Fore.WHITE+"============ INFORMACIÓN DE BUSES PCI ==========\n\n"+Style.RESET_ALL+Fore.YELLOW)
	subprocess.run("lspci", shell=True)
	sleep(5)
	borra_pantalla()
	print(Cursor.DOWN(5)+Cursor.FORWARD(5)+Back.RED+Fore.WHITE+"============ INFORMACIÓN DE PUERTOS USB ==========\n\n"+Style.RESET_ALL+Fore.YELLOW)
	subprocess.run("lsusb", shell=True)
	sleep(5)
	semaforo_total.release()

"""
red es una función que usando el módulo subprocess de python va a ejecutar
el comando (ifconfig) que nos da información sobre las tarjetas de red
de la computadora.
"""
def red():
	global semaforo_total
	semaforo_total.acquire()
	borra_pantalla()
	print(Cursor.DOWN(5)+Cursor.FORWARD(5)+Back.GREEN+Fore.WHITE+"=========== INFORMACIÓN DE TARJETA(S) DE RED ==========\n\n"+Style.RESET_ALL+Fore.GREEN)
	subprocess.run("ifconfig", shell=True)
	sleep(5)
	semaforo_total.release()
"""
sensores es una función que usando el módulo subprocess de python 
va a ejecutar el comando (sensors) que nos da  información sobre los 
sensores que hay en la computadora, dando datos de interés como la 
temperatura a la que se encuentra la computadora. 
"""
def sensores():
	global semaforo_total
	semaforo_total.acquire()
	borra_pantalla()
	print(Cursor.DOWN(5)+Cursor.FORWARD(5)+Back.MAGENTA+Fore.WHITE+"============ INFORMACIÓN DE LOS SENSORES ==========\n\n"+Style.RESET_ALL+Fore.MAGENTA)
	subprocess.run("sensors", shell=True)
	sleep(5)
	semaforo_total.release()
"""
ayuda es una función que proporciona información adicional acerca de las
opciones del menu de inicio
"""
def ayuda():
	borra_pantalla()
	print(Cursor.DOWN(5)+Cursor.FORWARD(5)+Back.BLUE+Fore.WHITE+"==================== AYUDA ===============\n\n"+Fore.WHITE)
	print(" 1 => Información de Sistema")
	print(Cursor.FORWARD(5)+"información sobre arquitectura, procesador, red, tipo, etc del sistema")
	print(" 2 => Información de Discos")
	print(Cursor.FORWARD(5)+"información sobre nombre, capacidad y montaje de discos del sistema")
	print(" 3 => Información de Procesos")
	print(Cursor.FORWARD(5)+"información sobre procesos en ejecución en el sistema")
	print(" 4 => Información de Memoria")
	print(Cursor.FORWARD(5)+"información sobre memoria RAM y memoria total del sistema")
	print(" 5 => Información de CPU")
	print(Cursor.FORWARD(5)+"información sobre arquitectura, numero, familia de la CPU del sistema")
	print(" 6 => Información de los buses PCI y los puertos USB")
	print(Cursor.FORWARD(5)+"información sobre los buses PCI y los puertos USB del sistema")
	print(" 7 => Información de la tarjeta de Red")
	print(Cursor.FORWARD(5)+"información sobre ip, dirección MAC de las tarjetas de red del sistema")
	print(" 8 => Información de los sensores de la máquina")
	print(Cursor.FORWARD(5)+"información sobre temperatura del sistema")
	print(" 9 => Análisis general del sistema")
	print(Cursor.FORWARD(5)+"Realiza todas las funciones anteriores")
	print(Cursor.FORWARD(5)+"\nPara seleccionar una opción teclea el número correspondiente y presiona la tecla enter ;) ")
	espera=input("\npresiona enter para volver al menu... ")
	print(Style.RESET_ALL)
"""
opcion es la función encargada de llamar a las demás funciones según lo 
seleccionado por el usuario
"""
def opcion(numero):
	if numero == "1":
		hilo=threading.Thread(target = sistema)
		hilo.start()
		hilo.join()
	elif numero == "2":
		hilo=threading.Thread(target = discos)
		hilo.start()
		hilo.join()
	elif numero == "3":
		mostrar_procesos_tiempo_real()
	elif numero == "4":
		hilo=threading.Thread(target = memoria)
		hilo.start()
		hilo.join()
	elif numero == "5":
		hilo=threading.Thread(target = cpu)
		hilo.start()
		hilo.join()
	elif numero == "6":
		hilo=threading.Thread(target = buses_puertos)
		hilo.start()
		hilo.join()
	elif numero == "7":
		hilo=threading.Thread(target = red)
		hilo.start()
		hilo.join()
	elif numero == "8":
		hilo=threading.Thread(target = sensores)
		hilo.start()
		hilo.join()
	elif numero == "9":
		analisis_general()
	elif numero == "h":
		ayuda()
	else:
		print(Fore.RED+"\topcion invalida...!")
		sleep(1)
		
		
"""
control es una función que muestra las opciones a elegir,
está siempre a la espera de una opción seleccionada por el usuario

"""
def control():
	global semaforo_total, borra
	borra_pantalla()
	print(Cursor.DOWN(2)+Cursor.FORWARD(10)+Style.BRIGHT+Fore.YELLOW+">>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<")
	print(Cursor.FORWARD(10)+">>>>>>>>>>>>>>>> MONITOR DE SISTEMA <<<<<<<<<<<<<<<<")
	print(Cursor.FORWARD(10)+">>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<")
	print(Cursor.FORWARD(10)+">>>>>>>>>>>>>>>>>> Realizado por: <<<<<<<<<<<<<<<<<<")
	print(Cursor.FORWARD(10)+">>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<")
	print(Cursor.FORWARD(10)+">>>>>>>>>>>> FLORES GASPAR JUAN ANTONIO <<<<<<<<<<<<")
	print(Cursor.FORWARD(10)+">>>>>>>>>>>>>>>>>>>>>>>>> Y <<<<<<<<<<<<<<<<<<<<<<<<")
	print(Cursor.FORWARD(10)+">>>>>>>>>>>>>>>> CORTES BENITEZ YAIR <<<<<<<<<<<<<<<")
	print(Cursor.FORWARD(10)+">>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<")
	while True:
		if(borra != 0):
			borra_pantalla()
		print(Cursor.DOWN(2)+Cursor.FORWARD(10)+Style.BRIGHT+Fore.BLUE+"********************* OPCIONES *******************\n")
		print(" 1 => Información de Sistema")
		print(" 2 => Información de Discos")
		print(" 3 => Información de Procesos")
		print(" 4 => Información de Memoria")
		print(" 5 => Información de CPU")
		print(" 6 => Información de los buses PCI y los puertos USB")
		print(" 7 => Información de la tarjeta de Red")
		print(" 8 => Información de los sensores de la máquina")
		print(" 9 => Análisis general del sistema")
		print(" h => AYUDA")
		print(" 0 => SALIR\n")
		numero=input(Fore.GREEN+" ~ $$"+Style.RESET_ALL)
		if numero== "0":
			break
		opcion(numero)
		borra+=1
		
		
"""
analisis general es una función que se llama en el caso de que el usuario seleccione 
análisis general del sistema, es la encargada de lanzar todos los hilos
para que se inicien las demás funciones y aqui se puede observar la sincronización de los 
hilos lograda con el mutex
"""		
def analisis_general():
	hilo=threading.Thread(target = sistema)
	hilo.start()
	hilo2=threading.Thread(target = discos)
	hilo2.start()
	hilo3=threading.Thread(target = procesos)
	hilo3.start()
	hilo4=threading.Thread(target = memoria)
	hilo4.start()
	hilo5=threading.Thread(target = cpu)
	hilo5.start()
	hilo6=threading.Thread(target = buses_puertos)
	hilo6.start()
	hilo7=threading.Thread(target = red)
	hilo7.start()
	hilo8=threading.Thread(target = sensores)
	hilo8.start()
	hilo8.join()#el join() es necesario porque sino al ejecutarse la funcion sensores, al terminar se queda a la
				#espera de un enter para regresar al menu de opciones.


control() #llamada a la función control para que muestre las opciones al usuario

