import os, shutil

##### Operaciones con Carpetas
def crearCarpeta():

	nomDirect = input("Dame el nombre del directorio que quieras crear ")
	validar = validarExistenciaCar(nomDirect)
	if validar == False:
		os.makedirs(nomDirect)
		print ("Directorio " + nomDirect + " Creado")
	else:
		print ("La carpeta ya existe...")
	menuCarpetas()

def validarExistenciaCarpeta():
	print ("Que directorio quieres validar?")
	nomDirect = input()
	decision = os.path.isdir(nomDirect)
	if decision == True:
		print ("El fichero " + nomDirect + " existe")
	else:
		print ("El fichero " + nomDirect + " no existe")
	menuCarpetas()

def validarExistenciaCar(nomDirect):
	result = os.path.isdir(nomDirect)
	return result

def eliminarCarpeta():
	print ("Que directorio deseas eliminar? ")
	nomDirect = input()
	validar = validarExistenciaCar(nomDirect)
	if validar == True:
		shutil.rmtree(nomDirect)
		print ("La carpeta " + nomDirect + " ha sido eliminada")
	else:
		print ("Carpeta inexistente...")
	menuCarpetas()

##### Final Operaciones con Carpetas


#####Operaciones con archivos

def crearArchivo():
	nomArch = input("Que nombre le deseas poner el archivos?")
	validar = validarExistenciaArch(nomArch)
	if validar == False:
		archivo = open (nomArch, "w")
		print("*******Recuerda que al ingresar la palabra 'salir' dejaras de ingresar texto al archivo*********")
		texto = input("Ingresa el Texto que deseas agregar \n")
		archivo.write(texto)
		while texto != "salir":
			texto = input()
			archivo.write("\n")
			archivo.write(texto)
		print ("El archivo " + nomArch + " ha sido creado con el texto asignado")
		menuArchivos()
	else:
		decision = input("El archivo ya existe, que operacion desea realizar? \n1)SobreEscribir \n2)EscribirAlFinal \n3)Salir")
		if decision == "SobreEscribir":
			archivo = open (nomArch, "w")
			texto = input("Ingresa el texto que deseas agregar")
			archivo.write(texto)
			while texto != "salir":
				texto = input()
				archivo.write("\n")
				archivo.write(texto)
			print ("Se agrego el texto")
			archivo.close()
			menuArchivos()
		elif decision == "EscribirAlFinal":
			archivo = open (nomArch, "a")
			archivo.write("\n")
			texto = input("Ingresa el texto que deseas agregar")
			archivo.write(texto)
			while texto != "salir":
				texto = input()
				archivo.write("\n")
				archivo.write(texto)
			print ("Se agrego el texto")
			archivo.close()
			menuArchivos()
		elif decision == "Salir":
				print ("Adios :D")
		else:
			print ("Operacion Invalida...")
			crearArchivo()

def eliminarArchivo():
	nomArch = input("Ingresa el archivo que deseas eliminar junto con su extencion")
	existe = validarExistenciaArch(nomArch)
	if existe == True:
		os.remove(nomArch)
		print ("El archivo " + nomArch + " ha sido eliminado correctamente")
	else:
		print ("Archivo inexistente...")
	menuArchivos()


def validarExitenciaArchivo():
	nomDirect = input("Que archivo quieres validar?")
	decision = os.path.isfile(nomDirect)
	if decision == True:
		print ("El archivo " + nomDirect + " existe")
	else:
		print ("El archivo " + nomDirect + " no existe")
	menuArchivos()


def validarExistenciaArch(nomArch):
	result = os.path.isfile(nomArch)
	return result

def mostrarContenidoArchi():
	nameArch = input("De que archivo deseas saber el contenido?")
	existe = validarExistenciaArch(nameArch)
	if existe == True:
		archivo = open(nameArch, 'r')
		contenido = archivo.read()
		print (contenido)
	else:
		print("El archivo no existe")
	menuArchivos()

def moverArchivo():
	nameArch = input("Cual es el nombre del archivo que deseas mover?")
	existe = validarExistenciaArch(nameArch)
	if existe == True:
		direccion = input ("Cual es la carpeta a la que deseas moverlo")
		existCarp = validarExistenciaCar(direccion)
		if existCarp == True:
			shutil.move(nameArch,direccion)
			print("El archivo "+ nameArch + "ha sido movido")
		else:
			print("DireccionInvalida")
	else:
		print("El archivo no existe... verificalo")
	menuArchivos()


###############Independiente
def directorioActual():
	direcActual = os.getcwd()
	print ("Ruta Actual: " + direcActual)

def ubicacionActual():
	ubicacion = os.getcwd()
	print (ubicacion)
	return ubicacion

def cambiarDirectorio():
	print("Para cambiar de Carpeta necesitas incluir todo el texto siguiente, mas la carpeta a la que deseas acceder")
	ubicacionActual()
	newUbicacion = input("Nueva Ubicacion")
	os.chdir(newUbicacion)
	ubicacionActual()

def listarContenido():
	hola = os.listdir()
	print(hola)

def ubicacionActual():
	ubicacion = os.getcwd()
	print(ubicacion)


#############################

########Menus de control

def menuAyuda():
	print("Menu de ayuda")
	print("Selecciona por numero la informacion que quieres obtener: ")
	decision = input("\n1)Ayuda con archivos \n2)Ayuda con carpetas \n3)Regresar")
	if decision == "1":
		archivo = open("ayudaArchivos.txt",'r')
		contenido = archivo.read()
		print(contenido)
		menuAyuda()
	elif decision == "2":
		archivo = open("ayudaCarpetas.txt", 'r')
		contenido = archivo.read()
		print(contenido)
	elif decision == "3":
		menuPrincipal()
		menuAyuda()
	else:
		print("Opcion invalida...")
		menuAyuda()

def menuArchivos():
	os.system("clear")
	print("Este apartado realiza las operaciones basicas con Carpetas")
	print ("Seleccion el numero de operacion que deseas realizar")
	decisiones = input ("\n1)Crear Archivo \n2)Leer Archivos \n3)Buscar Archivo \n4)Mover Archivo \n5)Eliminar Archivo \n6)Ubicacion \n7)Regresar\n")
	if decisiones == "1":
		crearArchivo()
	elif decisiones == "2":
		mostrarContenidoArchi()
	elif decisiones == "3":
		validarExitenciaArchivo()
	elif decisiones == "4":
		moverArchivo()
	elif decisiones == "5":
		eliminarArchivo()
	elif decisiones == "6":
		ubicacionActual()
	elif decisiones == "7":
		menuPrincipal()
	else:
		print("Comando invalido...")
		menuArchivos()

def menuCarpetas():
	os.system("clear")
	print("Este apartado realiza las operaciones basicas con Carpetas")
	print ("Seleccion el numero de operacion que deseas realizar")
	decisiones = input ("\n1)Crear Carpeta \n2)Buscar Carpeta \n3)Eliminar Carpeta \n4)Ubicacion \n5)Regresar\n")
	if decisiones == "1":
		crearCarpeta()
	elif decisiones == "2":
		validarExistenciaCarpeta()
	elif decisiones == "3":
		eliminarCarpeta()
	elif decisiones == "4":
		ubicacionActual()
	elif decisiones == "5":
		menuPrincipal()
	else:
		print("Comando invalido...")
		menuCarpetas()


def menuPrincipal():
	os.system("clear")
	print("Micro sistema de archivos")
	print("Seleccion opcion con su numero")
	dec = input("\n1)Menu de archivos \n2)Menu de carpetas \n3)Listar Contenido \n4)Cambiar de Carpeta \n5)Ubicacion \n6)Instrucciones \n7)Salir ")
	if dec == "1":
		menuArchivos()
	elif dec == "2":
		menuCarpetas()
	elif dec == "3":
		listarContenido()
		menuPrincipal()
	elif dec == "4":
		cambiarDirectorio()
		menuPrincipal()
	elif dec == "5":
		ubicacionActual()
	elif dec == "6":
		menuAyuda()
	elif dec == "7":
		print("Gracias por tu uso :D")
	else:
		print ("Comando incorrecto...")
		menuPrincipal()


def bienvenida():
	archivo = open("informacion.txt",'r')
	contenido = archivo.read()
	print (contenido)
	menuPrincipal()

bienvenida()
