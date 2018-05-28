# Sistemas de archivos remotos

    Tarea creada el 17.05.2018
	Entrega: 24.05.2018

En clase hicimos una breve mención de los sistemas de archivos
remotos, aunque no llegamos a abordarlos con detenimiento. En el libro
pueden encontrar el material al respecto [en la sección 6.5, de la
página 256 a la
260](http://sistop.org/pdf/sistemas_operativos.pdf#page=256).

El libro aborda dos sistemas de archivos remotos (el de los Unixes
tradicionales, *Network File System (NFS)*, y el que tradicionalmente
se relaciona con Windows que encontrarán bajo los nombres *Common
Internet File System (CIFS)* o *Server Message Block (SMB)*), y un
sistema de archivos distribuido, *Andrew File System (AFS)*.

## La tarea

En esta ocasión, la tarea consiste en un documento corto, un pequeño
reporte de 1 o 2 páginas de longitud. Les pido que identifiquen *otro*
sistema de archivos remoto o distribuido (ninguno de los tres
anteriores). Cuéntenme de qué se trata este sistema de archivos,
particularmente:

- ¿Es _remoto_ o _distribuido_? ¿Por qué sienten que sea así?
- ¿Cuáles son sus características principales? ¿Para qué tipo de uso
  está diseñado?
- ¿Para qué sistema operativo está diseñado? ¿Saben si está
  implementado en algún otro sistema?
- ¿Cómo es su _modelo de fallos_ o _modelo de consistencia_? (para una
  mejor explicación de a qué me refiero con esto, revisen la
  definición de AFS — Más allá de los primeros dos párrafos que
  presentan al sistema, casi todo el resto es referente a su modelo de
  consistencia).

Algunos ejemplos de sistemas de archivos remotos en boga hoy en día
son GlusterFS y CEPH (desarrollados ambos por RedHat), S3 (de Amazon),
GoogleFS (de Google, naturalmente) y Windows Distributed File System
(de Microsoft). En clase les mostré brevemente el uso de `sshfs`, que
está construido sobre `FUSE`. Pero hay muchos, muchísimos más que
pueden abordar.

## Referencias

En clase les mencioné dos artículos que se publicaron hoy en 
[LWN.net](https://lwn.net/) relacionados con este tema: Esta semana se
celebra el 2018 Linux Storage, Filesystem, and Memory-Management Summit
(LSFMM). De la cobertura que les hace LWN,

- [Network filesystem topics](https://lwn.net/SubscriberLink/754506/f312df34b988f603/)
- [SMB/CIFS compounding support](https://lwn.net/SubscriberLink/754507/98c73dcca48f0d0c/)

## Entrega

La entrega puede hacerse de forma individual o en equipos de dos
personas. Utilicen la ya habitual nomenclatura y ubicación estándar
para todas sus entregas mediante Git.

## Calificaciones y comentarios

[Disponibles en el archivo calificaciones.org](./calificaciones.org)
