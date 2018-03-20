"""
SISTEMAS OPERATIVOS
TAREA 2: Solucion al problema de los gatos y los ratones 
//INTEGRANTES : CORTES BENITEZ YAIR // FLORES GASPAR JUAN ANTONIO
"""
import threading
import time
import random
mutex = threading.Semaphore(1)  # Para proteger a linea_de_platos
mutex2 = threading.Semaphore(1) # Para proteger a comiendo
hay_platos = threading.Semaphore(0)#para proteger pongo plato
linea_de_platos = []#para guardar los platos de comida generados 
animales = []#para guardar los gatos y ratones generados 
comiendo = 0#para saber si alguien come
maximo_de_comelones = 1#para que no coma mas de uno a la vez
estan_comiendo = threading.Semaphore(0)#para proteger quien come
acabado = 0#para los platos que ya se comieron 

class plato:
    def __init__(self):
        self.plato = random.random()
        print ("Generando plato con comida numero %1.3f" % self.plato)
        time.sleep(self.plato*1/3)
    def comido(self):
        numero=self.plato
        time.sleep(self.plato*2/3)
        return(numero)
class gatitos:
    def __init__(self):
        self.gatitos = random.random()
        print ("Generando al gato numero %1.3f" % self.gatitos)
        time.sleep(self.gatitos)
    def numero(self):
        numero=self.gatitos
        return(numero)
class ratoncitos:
    def __init__(self):
        self.ratoncitos = random.random()
        print ("Generando al raton numero %1.3f" % self.ratoncitos)
        time.sleep(self.ratoncitos)
    def numero(self):
        numero=self.ratoncitos
        return(numero)
    

def pongo_plato():
    global comiendo
    global maximo_de_comelones
    global acabado
    while True:
        numero = plato().comido()
        evento = plato()#ponemos un plato con comida
        mutex2.acquire()
        if comiendo < 0:#esto se hace porque algunas veces la variable comiendo tomaba valores negativos
            comiendo=0
        if comiendo == maximo_de_comelones:
            mutex2.release()
            if(acabado != 0):#si ya hay platos comidos se indica
                print ("***Alguien comio el plato (%1.3f)" % acabado)
            estan_comiendo.acquire()
        else:
            mutex2.release()
            print ("*Puede alguien comerse el plato (%1.3f)" % numero)
            comiendo += 1

        mutex.acquire()
        linea_de_platos.append(evento)
        if (len(animales) != 0):
            anim=animales.pop()#se saca al animal que ya comio
        mutex.release()
        hay_platos.release()#se libera el semaforo porque ya hay un plato disponible

def gato():
    global comiendo
    global maximo_de_comelones
    global acabado
    while True:
        numero = plato().comido()
        evento=gatitos()#se generan gatos 
        animal_n = gatitos().numero()
        hay_platos.acquire() #se adquiere el semaforo para comer
        mutex2.acquire()
        if comiendo == maximo_de_comelones:#si hay oportunidad de comer 
            print ("\tSoy el GATO (%1.3f) tengo hambre, me estoy comiendo el plato (%1.3f)"%(animal_n,  numero))
            acabado = numero#para saber que plato fue comido
            estan_comiendo.release()
        mutex2.release()
        mutex.acquire()
        comiendo -= 1
        animales.append(evento)#se agrega al gato generado
        plat = linea_de_platos.pop()#se saca el plato comido
        mutex.release()
def raton():
    global comiendo
    global maximo_de_comelones
    global acabado
    while True:
        numero = plato().comido()
        evento= ratoncitos()#se generan ratones 
        animal_n=ratoncitos().numero()
        hay_platos.acquire()#se adquiere el semaforo para comer 
        mutex2.acquire()
        if comiendo == maximo_de_comelones:#si hay oportunidad de comer 
            print ("\t\tSoy el RATON (%1.3f) tengo hambre, voy a comer! (%1.3f)" % (animal_n, numero))
            acabado = numero#para saber que plato fue comido
            estan_comiendo.release()
        mutex2.release()
        mutex.acquire()
        comiendo -= 1
        animales.append(evento)#se agrega al raton generado
        plat = linea_de_platos.pop()#se saca el plato comido
        mutex.release()
#inicio de hilos
threading.Thread(target=pongo_plato, args=[]).start()
threading.Thread(target=gato, args=[]).start()
threading.Thread(target=raton, args=[]).start()
