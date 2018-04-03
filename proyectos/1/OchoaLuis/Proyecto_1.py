# -*- coding: utf-8 -*-

# El programa que sigue es para el proyecto # 1 de la materia de Sistemas Operativos 
# Impartida por Gunnar Wolf para el Semestre 2018-2 de la FI - UNAM

#--------------------------------------

# Debido a que me clave en el uso de tkinter y no le dediqué mucho tiempo a multiprocesos, 
# Realicé una miniaturización lo más posible de mi código. Decidí aprdener un poco más de Tkinter.
# de los multiprocesos no es mucho son 20 lineas no creo necesitar más ...


import multiprocessing
import time
import Tkinter as tk
import ttk
import AppKit


#------Código de los multiprocesos____
#Proceso cualquiera...
def process(x):
	t = 0
	while t < 10:
		print "Running ", x, "-", t
		t +=1
		time.sleep(x)

class MonitorApp(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.pack()

        self.master.title(" Monitor App ")
        self.master.geometry('600x400+1000+500')

        lorem_ipsum = "Pantalla para correr el monitor del sistema\n" \
                      "Facultad de Ingeniería\n" \
                      

        tk.Label(self, text="This is a message (under a label)").pack()

        tk.Message(self, text=lorem_ipsum, justify='left').pack(pady=(10, 10))

class ThreadApp(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.pack()

        self.master.title(" Thread App ")
        self.master.geometry('600x400+1000+500')

        lorem_ipsum = "Pantalla para correr: Multihilos." \

        tk.Label(self, text="This is a message (under a label)").pack()

        tk.Message(self, text=lorem_ipsum, justify='left').pack(pady=(10, 10))


#------Código con repecto a la GUI -----
class MultiprocessApp(tk.Frame):

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.pack()

        self.master.title(" Multiprocesos ")
        self.master.geometry('600x400+1000+500')

        message = "Universidad Nacional Autónoma de México \n" \
                  "Facultad de Ingeniería\n" \
                  "Sistemas Operativos 2018-2\n" \
                  "Profesor: Gunnar Eyal Wolf Iszaevich\n" \
                  "Presenta: Ochoa Ríos Luis Ernesto\n\n" \
                  "Su única función es lanzar 2 procesos para que sean realizados con la librería de multiprocessing de python.\n" \
                  "Agregue a éste programa una GUI con Tkinter y de ahí en fuera es muy simple.\n"

        tk.Message(self, text=message, justify='left').pack(pady=(10, 10))

        tk.Label(self, text="Presione botón para correr procesos:").pack()
        tk.Button(self, text='OK', command=self.ok).pack()



    def ok(self):
        p1 = multiprocessing.Process(target=process, args=(1,))
        p2 = multiprocessing.Process(target=process, args=(2,))

        p1.start()
    	time.sleep(0.5)
    	p2.start()


        while True:
        	if not p2.is_alive():
            		p1.terminate()
            		break
        print "Both processes finished"


if __name__ == '__main__':

    root = tk.Tk()

    app = MultiprocessApp(root)

    top1 = tk.Toplevel(root)
    ThreadApp(top1)

    top2 = tk.Toplevel(root)
    MonitorApp(top2)

    AppKit.NSApplication.sharedApplication().activateIgnoringOtherApps_(True)

    app.mainloop()


# Hecho en México, CDMX 