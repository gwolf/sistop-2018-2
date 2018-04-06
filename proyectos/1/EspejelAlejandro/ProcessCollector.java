import java.util.concurrent.Semaphore;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.io.File;
import java.io.BufferedReader;

//Clase que obtiene la imformacion a desplegar.

class ProcessCollector extends Thread {

	String ruta = "/proc/meminfo";
	String var;
	String etiqueta;
	int id;
	int num_hilos_escribiendo = 0;
	
	Semaphore mutex;
	Semaphore barrera;
	Semaphore torniquete;
	Semaphore puedesImprimir;
	int num_hilos = Coordinator.getNumColectores();
	int cuenta;

	ProcessCollector(int id, String var, String eti, Semaphore mutex, Semaphore barrera, Semaphore torniquete, Semaphore puedesImprimir){
		this.var = var;
		this.id = id;
		this.etiqueta = eti;
		this.mutex = mutex;
		this.barrera = barrera;
		this.torniquete = torniquete;
		this.puedesImprimir = puedesImprimir;
	}

	public void run(){

		//torniquete para funcionamiento
		try{
			torniquete.acquire();
		}catch(Exception e){
			e.printStackTrace();
		}
		torniquete.release();
        String cadena;
        try{
        	FileReader f = new FileReader(ruta);
        	BufferedReader b = new BufferedReader(f);
        	while((cadena = b.readLine())!=null) {
	        	if (cadena.startsWith(var))
	        		agregaDatos(cadena);
        	}
        b.close();
		}catch(Exception e){
        	e.printStackTrace();
        }
        if(num_hilos_escribiendo == 0)
        	puedesImprimir.release();
	}

    //Implementación de la barrera
    public void agregaDatos(String cadena){

    	num_hilos_escribiendo++;
    	
    	String aux = daFormato(cadena);

    	try{
    		mutex.acquire();
    	}catch(Exception e){
    		e.printStackTrace();
    	}
    	Coordinator.addCuenta();
    	mutex.release();

    	if(Coordinator.getCuenta() == num_hilos)
    		barrera.release();

    	try{
    		barrera.acquire();
    	}catch(Exception e){
    		e.printStackTrace();
    	}
    		barrera.release();
		Coordinator.addDato(id,aux);
		Coordinator.colectoresListos.release();

		num_hilos_escribiendo--;
    }

	public String buscarNumero(String cadena){
    	String aux = "";
        char[] arreglo = cadena.toCharArray();
        for (char caracter : arreglo){
            if (Character.isDigit(caracter))
                aux = aux + caracter;
        }   
        return aux;
    }

    public String daFormato(String cadena){
    	String aux = buscarNumero(cadena);
    	return etiqueta.concat(": "+aux+" kb");
    }
}
