nombres de los participantes:
Lozano Estrada Ruben Omar
Ramirez Gonzalez Jesus Alejandro

problema que busca resolver:
la necesidad de tener en un solo programa varios mas disponibles, para poder revisar informacion que consideramos importante del sistema operativo para su facil acceso a ella(monitoreo).

logica de operacion:
ejecuta un modulo dependiendo la informacion que se quiere consultar y te regresa dicha informacion

ejemplo de uso o invocacion:
	1. abrimos la terminal y cambiamos al directorio /proyectos/1/lozanoRuben-RamirezAlejandro/ donde está el archivo monitor.py y  lo ejecutas con la siguiente linea "python3 monitor.py" y se abre la interfaz de la aplicacion en la cual puedes teclear cualquier comando disponible
	2. ingresar un comando de acuerdo a lo que se desea obtener acerca de la informacion del sistema operativo
	3. te entrega la informacion correspondiente y regresa el control al proceso monitor

	Documentacion

	*Al momento de teclear help seguido de cualquier comando disponiponible (help <comando>)se muestra brevemente la descripcion del comando y la informacion que devuelve hacerca de sistema.


		a)all:Desliega toda la informacion del sistema disponible

		b)disk:Desliega el uso de disco por directorio, incluyendo los subdirecctorios del mismo.

		c)memory: Muestra informacion sobre la memoria de la maquina. Incluye memoria RAM, swap y buffers usados por el kernel. Ademas despliega el contenido del archivo /proc/meminfo
		
		d)process:Muestra los procesos que estan corriendo en ese momento con informacion especifica de cada uno.

		e)protree:Despliega lo procesos que estan corriendo en ese momento en formato de arbol.

		f)logins:Imprime los logins del sistema.
		
		g)cpuinfo:Imprime los logins del sistema.

		h)interrupts:Imprime las interrupciones a los cpu's. Funciona gracias al archivo /proc/interrupts

		i)clear:Limpia la pantalla

		j)help:Comando para desplegar informacion sobre los comandos.


