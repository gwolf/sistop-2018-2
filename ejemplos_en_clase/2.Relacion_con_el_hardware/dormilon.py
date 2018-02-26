#!/usr/bin/python
# -*- Encoding: UTF-8
#
# Este programita lo usamos para ver cómo se implementa la
# (aparentemente sencilla) llamada al sistema "sleep()". Llámalo
# mediante el programa strace ($ strace python dormilon.py).
#
# Llama la atención lo _larga y complicada_ que es la inicialización
# de Python. Ya después de eso, verás que la lógica del programa
# centrado en sus llamadas al sistema es muy sencilla:
#
# write(1, "Hola mundo!\n", 12)           = 12
# select(0, NULL, NULL, NULL, {tv_sec=1, tv_usec=0}) = 0 (Timeout)
# write(1, "Me gusta dormir todo el tiempo d"..., 58) = 58
# select(0, NULL, NULL, NULL, {tv_sec=3, tv_usec=0}) = 0 (Timeout)
# write(1, "Pero lleg\303\263 el momento de salir."..., 39) = 39
# rt_sigaction(SIGINT, {sa_handler=SIG_DFL, sa_mask=[], sa_flags=SA_RESTORER, sa_restorer=0x7fa86aa4b0c0}, {sa_handler=0x557354d56a70, sa_mask=[], sa_flags=SA_RESTORER, sa_restorer=0x7fa86aa4b0c0}, 8) = 0
# exit_group(0)                           = ?
# +++ exited with 0 +++

from time import sleep

print "Hola mundo!"
sleep(1)
print "Me gusta dormir todo el tiempo de ejecución que puedo..."
sleep(3)
print "Pero llegó el momento de salir. Chau!"
