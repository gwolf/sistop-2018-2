"""
Micro sistema de archivos
Sistemas Operativos
creado por: Flores Gaspar Juan y Cortes Benitez Yair
"""
import os
from colorama import Fore, init, Style, Back, Cursor	#para cambiar de color y formato las impresiones en consola //no es estandar
import subprocess
from time import sleep
borra=0
reg=0
numreg=0
disco_temp=[]
conta_lin_ti=0
conta_lin_tf=0
conta_lin_ci=0
conta_lin_cf=0

def borra_pantalla(): #función para limpiar la consola
	subprocess.run("clear", shell=True)
"""
La función archivo_base verifica si existe el archivc en donde se guardan los
datos, de no existir crea el archivo
"""
def archivo_base():
	try:
		archivo=open('.disco.dat', 'r')
		archivo.close()
	except FileNotFoundError:
		print(Fore.RED+"\tArchivo base no encontrado..!!")
		print(Fore.GREEN+"\tCreando archivo..!")
		sleep(2)
		archivo=open('.disco.dat', 'w')
		divide="#%TABLAI%#\n\n#%TABLAF%#\n\n@&CONTENIDOI&@\n\n@&CONTENIDOF&@\n0"
		archivo.write(divide)
		archivo.close()
"""
La función lista es la encargada de listar todos los nombres de archivos 
existentes
"""		
def lista():
	global disco_temp, conta_lin_ti, conta_lin_tf, conta_lin_ci, conta_lin_cf, reg, numreg
	lista_archivos=[]
	lee_disco()
	referencias()
	for x in disco_temp[conta_lin_ti+1:conta_lin_tf]:
		lista_archivos.append(x)
	conta=1
	tamano=len(lista_archivos)	
	while conta<tamano:
		print(lista_archivos[conta])
		conta+=2
	del disco_temp[:]
	sleep(5)


"""
La función agrega se encarga de agregar contenido a un archivo existente
"""	
def agrega(nombre, conte):
	global disco_temp, conta_lin_ti, conta_lin_tf, conta_lin_ci, conta_lin_cf, reg, numreg
	lee_disco()
	referencias()
	nombre= nombre+'\n'
	existe= nombre in disco_temp[conta_lin_ti+1:conta_lin_tf]
	if existe:
		bloque=disco_temp.index(nombre)-1
		dire_principal=disco_temp.pop(bloque)
		direccion='#'+ dire_principal
		bloque_cont=disco_temp.index(direccion)+1
		contenido=str(disco_temp.pop(bloque_cont))
		salto=contenido.find('\n')
		contenido=contenido[:salto]+' '
		nuevo_contenido=contenido+conte+'\n'
		bloque_cont=disco_temp.index(direccion)+1
		disco_temp.insert(bloque_cont ,nuevo_contenido)
		bloque=disco_temp.index(nombre)
		disco_temp.insert(bloque , dire_principal)
		escribe_disco()
	else:
		print(Fore.RED+"\tNo existe el archivo...!")
		sleep(1)
		del disco_temp[:]
"""
La función lee_disco se encarga de leer linea a linea el archivo en donde
se guardan los datos y crea una lista para que se pueda modificar su contenido
"""
def lee_disco():
	global disco_temp
	archivo=open('.disco.dat', 'r')
	while True:
		linea=archivo.readline()
		disco_temp.append(linea)
		if not linea:
			break
	archivo.close()
"""
La función escribe_disco se encarga de convertir a texto la lista de datos
modificada y guardarla en el archivo de datos
"""
def escribe_disco():
	global disco_temp
	escribe = "".join(disco_temp)
	archivo=open('.disco.dat', 'w')
	archivo.write(escribe)
	archivo.close()
	del disco_temp[:]
"""
La función referencias encuentra los limites de la tabla de nombres y la tabla de
contenidos, asi como de obtener el ultimo numero de registro guardado en el archivo
"""	
def referencias():
	global disco_temp, conta_lin_ti, conta_lin_tf, conta_lin_ci, conta_lin_cf, reg
	conta_lin_ti=disco_temp.index("#%TABLAI%#\n")
	conta_lin_tf=disco_temp.index("#%TABLAF%#\n")
	conta_lin_ci=disco_temp.index("@&CONTENIDOI&@\n")
	conta_lin_cf=disco_temp.index("@&CONTENIDOF&@\n")
	reg=disco_temp.index("@&CONTENIDOF&@\n")+1
"""
La función nuevo se encarga de crear un archivo nuevo y asociarle una direccion unica de 
referencia
"""
def nuevo(nombre, conte):
	global disco_temp, conta_lin_ti, conta_lin_tf, conta_lin_ci, conta_lin_cf, reg, numreg
	lee_disco()
	if nombre+'\n' in disco_temp:
		print(Fore.RED+"\tYa existe un archivo con ese nombre...!")
		sleep(1)
		del disco_temp[:]
	else:
		referencias()
		numreg=int (disco_temp.pop(reg))
		del disco_temp[reg]
		disco_temp.insert(conta_lin_tf-1, '#xx'+str(numreg)+'\n' + nombre +'\n')
		disco_temp.insert(conta_lin_cf, '##xx'+str(numreg)+'\n' + conte+'\n')
		numreg+=1
		disco_temp.append(str (numreg))
		escribe_disco()
"""
La función borra se encarga de eliminar el nombre y contenidos de un archivo asi como su 
direccion de referencia
"""
def borrar(nombre):
	global disco_temp, conta_lin_ti, conta_lin_tf, conta_lin_ci, conta_lin_cf, reg, numreg
	lee_disco()
	referencias()
	nombre= nombre+'\n'
	existe= nombre in disco_temp[conta_lin_ti+1:conta_lin_tf]
	if existe:
		archi=disco_temp.index(nombre)#borra
		bloque=disco_temp.index(nombre)-1
		direccion='#'+ disco_temp.pop(bloque)
		dire_cont=disco_temp.index(direccion)
		bloque_cont=disco_temp.index(direccion)+1#borra
		del disco_temp[bloque_cont]
		archi=disco_temp.index(nombre)#borra
		bloque=disco_temp.index(nombre)-1
		dire_cont=disco_temp.index(direccion)
		del disco_temp[dire_cont]
		archi=disco_temp.index(nombre)#borra
		del disco_temp[archi]
		escribe_disco()
	else:
		print(Fore.RED+"\tNo existe el archivo...!")
		sleep(1)
		del disco_temp[:]

"""
La función ver muestra el contenido de un archivo
"""
def ver(nombre):
	global disco_temp, conta_lin_ti, conta_lin_tf, conta_lin_ci, conta_lin_cf, reg, numreg
	lee_disco()
	referencias()
	nombre= nombre+'\n'
	existe= nombre in disco_temp[conta_lin_ti+1:conta_lin_tf]
	if existe:
		bloque=disco_temp.index(nombre)-1
		direccion='#'+ disco_temp.pop(bloque)
		bloque_cont=disco_temp.index(direccion)+1
		#print(bloque_cont)
		contenido=disco_temp.pop(bloque_cont)
		print(contenido)
		sleep(5)
		del disco_temp[:]
	else:
		print(Fore.RED+"\tNo existe el archivo...!")
		sleep(1)
		del disco_temp[:]
		

def ayuda():
	borra_pantalla()
	print(Cursor.DOWN(5)+Cursor.FORWARD(5)+Back.BLUE+Fore.WHITE+"==================== AYUDA ===============\n\n"+Fore.WHITE)
	print(" lista => lista todos los archivos existentes")
	print(Cursor.FORWARD(5)+"Ejemplo: ~ $$lista ")
	print(" agrega => Agrega una cadena a un archivo")
	print(Cursor.FORWARD(5)+"Ejemplo: ~ $$agrega mi_archivo.txt 'Mi nombre'")
	print(Cursor.FORWARD(5)+"La cadena debe ir entre comillas simples si contiene algun espacio")
	print(" nuevo => Crea un archivo")
	print(Cursor.FORWARD(5)+"Ejemplo: ~ $$nuevo mi_archivo.txt 'Mi nombre'")
	print(Cursor.FORWARD(5)+"La cadena debe ir entre comillas simples si contiene algun espacio")
	print(" borra => Borra un archivo")
	print(Cursor.FORWARD(5)+"Ejemplo: ~ $$borra mi_archivo.txt")
	print(" ver => Muestra el contenido de un archivo")
	print(Cursor.FORWARD(5)+"Ejemplo: ~ $$ver mi_archivo.txt")
	print(Cursor.FORWARD(5)+"\nPara seleccionar una opción teclea el número correspondiente y presiona la tecla enter ;) ")
	espera=input("\npresiona enter para volver al menu... ")
	print(Style.RESET_ALL)
"""
La función opcion se encarga de llamar a la opcion pedida por el usuario
ademas de llamar a la funciñon archivo_base para que siempre exista el 
archivo de datos
"""
def opcion(opc):
	archivo_base()
	primer_espacio=opc.find(" ")
	if opc == "lista" or opc == "ayuda":
		primer_espacio=5
		comando=opc[:primer_espacio]
	comando=opc[:primer_espacio]
	if comando=="ver":	
		nombre=opc[primer_espacio+1:]
	elif comando=="borra":
		nombre=opc[primer_espacio+1:]
	else:
		comando=opc[:primer_espacio]
		opc=opc[primer_espacio+1:]
		segundo_espacio=opc.find(" ")
		nombre=opc[:segundo_espacio]
		conte=opc[segundo_espacio+1:]
	if comando == "lista":
		lista()
	elif comando == "agrega":
		agrega(nombre, conte)
	elif comando == "nuevo":
		nuevo(nombre, conte)
	elif comando == "borra":
		borrar(nombre)
	elif comando == "ver":
		ver(nombre)
	elif comando == "ayuda":
		ayuda()
	else:
		print(Fore.RED+"\topcion invalida...!")
		sleep(1)
"""
La función control muestra las opciones al usuario
"""
def control():
	global borra
	borra_pantalla()
	print(Cursor.DOWN(2)+Cursor.FORWARD(10)+Style.BRIGHT+Fore.YELLOW+">>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<")
	print(Cursor.FORWARD(10)+">>>>>>>>>>> (Micro) Sistema de archivos <<<<<<<<<<<<")
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
		print(" lista                                => Lista archivos")
		print(" agrega <nombre de archivo> 'cadena'  => Agrega una cadena a un archivo")
		print("  nuevo <nombre de archivo> 'cadena'  => Crea un archivo")
		print("  borra <nombre de archivo>           => Borra un archivo")
		print("    ver <nombre de archivo>           => Muestra el contenido de un archivo")
		print("  ayuda                               => AYUDA")
		print("  salir                               => SALIR\n")
		opc=input(Fore.GREEN+" ~ $$"+Style.RESET_ALL)
		if opc== "salir":
			break
		opcion(opc)
		borra+=1

control()


