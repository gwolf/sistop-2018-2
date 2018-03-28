# README para la presentación: ¿Alguien dijo Keylogger?
<center>

![Python logo](https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg)

</center>



CREADO POR: 

Ochoa Ríos Luis Ernesto 

Palomeque González José Alonso			
<div style="text-align: right">Para el curso **Sistemas Operativos - Semestre 2018-2** </div>


##Requerimientos
El sistema operativo en el cual se probó el código fué en un **Windows 7 con SP2** y **Python 2.7.12** instalado y las diversas librerías que se nombraran a continuación:

   * **pyWin32** 
   * **pyHook**
   * **WMI**

Para el objetivo de la presentación, se eligió el Sistema Operativo Windows ya que es el más común utilizado por la mayoría de los alumnos y de los usuarios promedio. 

##Descripción del proyecto
Se desarrolla un pequeño programa en Python para realizar un Keylogger (monitor de teclas pulsadas), éste programa de Python no sólo monitorea los recursos del Sistema Operativo sino que también recolecta reportes de las aplicaciones abiertas, toma screenshots del Sistema y en un archivo de texto almacena las teclas pulsadas.

El programa es obtenido del libro **Learning Python for Forensics**, lo explico en la presentación pero bien pueden leer el capítulo 10 del mismo.  

Los pequeños programas que encontrarás en esta carpeta tienen la finalidad de enseñar, con ejemplos muy sencillos, que librerías del Sistema Operativo se van a utilizar en el programa final. 

##Instalación de Herramientas (Detalles a considerar)

En mi Sistema Operativo no estaba instalado Python (no se porque), lo debí de haber desinstalado o algo por el estilo. Si no lo tienes instalado dirigirte a
["Repositorio de instaladores de Python"](https://www.python.org/downloads/release/python-2712/) y podrás instalarlo en el Sistema Operativo que desees.

Para poder ver que versión de Python tienes, hay que teclear en una terminal

 `python --version`

Instalé el 2.7.12 para que estuviese acorde al programa que se explica en el libro **Learning Python for Forensics**. Las librerías debes instalarlas, para ello seguir los siguientes pasos...

##Instalación de librerías

 Ir al siguiente [enlace](https://www.lfd.uci.edu/~gohlke/pythonlibs/).
 
 Buscar en la página web, las librerías de **pyHook** y **pyWin32**. 
 
 Descargarlas siguiendo el siguiente criterio:
 
 Si tienes instalado Python2.7 y un SO de 32 bits 
 Elige -cp27-win32. 
 Por ende cp indica la versión de Python que tengas instalado en tu SO.
 **Win32** indica si tu SO es de 32 bits y **Win_amd64** si tu SO es de 64 bits.
 
Una vez que hayas descargado los archivos **.whl** tanto de **pyWin32** y **pyHook** deberás relocalizarlos en la siguiente carpeta 

`C:/python27/Scripts` 

(consideren que el nombre de la carpeta depende de la version de python que tengan instalado en su SO).

Abrir una línea de comando y localizarse en la carpeta 

**C:\python27\Scripts**  

Ejecutar el siguiente comando: 

`pip install some-package.whl`

Reemplazar el nombre some-package por el nombre de las librerías que deseas instalar.

**Puede que te aparezca un mensaje de que debes de actualizar pip, en el mismo mensaje te dicen la línea a ejeutar para actualizar el instalador...**

Una vez instaladas las 2 librerías, finalizamos para instalar **WMI**  que ya está en un hermoso instalador hasta el final de la siguiente [página web](https://pypi.python.org/pypi/WMI/#downloads).

Con esto tendrías las 3 librerías, **pyWin32, pyHook y  WMI**, las cualés son las más importantes que vamos a ocupar en el desarrollo del programa. 



-----

Fecha de creación (v1.0): 27 de Marzo de 2018

Hecho en México, CDMX. 

## Licenciamiento ##

El código de los programas fueron obtenidos del libro **Learning Python for Forensics** de Preston Miller y Chapin Bryce, de la editorial Packt Publishing. También podrás localizar el código del mismo en el siguiente repositorio [Repositorio de "Learning Python for Forensics"](https://github.com/PacktPublishing/Learning-Python-for-Forensics).



La presentación pueden utilizarla como parte de la norma de
 _Creative Commons Attribution 4.0 International_
 
[CC BY 4.0](https://creativecommons.org/licenses/?lang=es)

![CC BY ](https://mirrors.creativecommons.org/presskit/buttons/88x31/svg/by.svg)



Puedes [consultar el texto completo de la licencia](./COPYING.md).

La originalidad y autoría de cada elemento contenido en el repositorio
es responsabilidad de quien lo registró (alumno o profesor).
