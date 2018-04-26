#!/usr/bin/python
#
# Este programa ilustra cómo se mapea a memoria un archivo.  El
# ejemplo que mostré en clase era un poco más sencillo, pues usaba el
# modo default de acceso (rw-s). Aquí genero un par de mapeos
# diferentes resultando en distintos permisos.
from mmap import *
from time import sleep

# Vamos a abrir un archivo del sistema. En un sistema Debian
# o derivado, tendrán el texto de la licencia GPL-3 (35KB):
#
# Hay que abrirla para sólo lectura, pues no tenemos permisos para
# modificar el archivo.

licencia = '/usr/share/common-licenses/GPL-3'
lectura = open(licencia, 'r')
mapa1 = mmap(lectura.fileno(), 0, MAP_SHARED, PROT_READ)

# Abrimos un archivo de 1GB, para lectura/escritura. El archivo no
# necesariamente existe - Basta el seek/write/flush para que ocupe el
# espacio que queramos.
archivote = open('/tmp/archivote', 'w+')
seek(archivote, 1024*1024*1024)
archivote.write(' ')
archivote.flush()
mapa2 = mmap(archivote.fileno(), 1024*1024*1024)

# Incluso podemos darle -1 en vez de un archivo abierto para asignar
# un _espacio anónimo_ del tamaño que necesitemos. ¿Les gustan 4GB?
mapa3 = mmap(-1, 4*1024*1024*1024)

print mm[15000:15100]
sleep(600)
