

from threading import Semaphore, Thread
from time import sleep 


numHackerslinux = 0  
numSerfsmicro = 0    
numpasajeros = 0   
filaHackers = Semaphore(0) 
filaSerfs = Semaphore(0)   
mutex = Semaphore(1)        
mutexBals = Semaphore(1)  

def hackerlinux():             
    global numHackerslinux
    global numSerfsmicro
    mutex.acquire()
    numHackerslinux+=1
    if numHackerslinux==4:       
        filaHackers.release() 
        filaHackers.release()
        filaHackers.release()
        numHackerslinux-=4         
        mutex.release()      
        sube("Hackerlinux")     
        
    elif (numHackerslinux==2 and numSerfsmicro==2): 
        filaHackers.release()            
        filaSerfs.release()
        filaSerfs.release()
        numHackerslinux-=2                    
        numSerfsmicro-=2
        mutex.release()                      
        sube("Hackerlinux")                 
    else:
        
        mutex.release()                   
        filaHackers.acquire()            
        sube("Hackerlinux")                 

def serfmicro():
    global numHackerslinux
    global numSerfsmicro
    mutex.acquire()
    numSerfsmicro+=1
    
    if numSerfsmicro==4:
        filaSerfs.release()
        filaSerfs.release()
        filaSerfs.release()

        numSerfsmicro-=4
        mutex.release()
        sube("Serfmicro")
    elif (numHackerslinux==2 and numSerfsmicro==2):
        filaHackers.release()
        filaHackers.release()
        filaSerfs.release()
        numHackerslinux-=2
        numSerfsmicro-=2
        mutex.release()
        sube("Serfmicro")
    else:
        mutex.release()
        filaSerfs.acquire()
        sube("Serfmicro")


def sube(pasajeroac):
    global numpasajeros
    mutexBals.acquire()
    numpasajeros+=1
    print("Soy un "+pasajeroac+" y estoy arriba")
    if numpasajeros==4:
        avanzar()
        numpasajeros=0

    mutexBals.release()

def avanzar():
    print("--Avancemos!")
    sleep(1)

for i in range(16):
    Thread(target = hackerlinux, args = []).start()
    Thread(target = hackerlinux, args = []).start()
    Thread(target = serfmicro, args = []).start()
    