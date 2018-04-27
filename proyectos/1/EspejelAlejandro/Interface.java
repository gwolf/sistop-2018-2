import java.util.concurrent.Semaphore;

//Clase que le da formato a la salida de los datos

class Interface extends Thread {
	
	static final int WIDE = 60;
	private Semaphore torniquete;
	private Semaphore puedesImprimir;
	
	Interface(Semaphore torniquete, Semaphore puedesImprimir){
		this.torniquete = torniquete;
		this.puedesImprimir = puedesImprimir;
	}

	public void run(){
		dibujaVentana();
	}

	private void dibujaVentana(){	

		clear();
		for (int i = 0; i <= WIDE; i++) {
			System.out.print("=");
		}
		System.out.println();
		//bloqueo del torniquete de los colectores
		try{
			torniquete.acquire();
		}catch(Exception e){
			e.printStackTrace();
		}
		//verifica que no haya hilos colectores escribiendo
		try{
			puedesImprimir.acquire();
		}catch(Exception e){
			e.printStackTrace();
		}

		for(int i = 0; i < SystemMonitor.sizeDatos(); i++){
			//Columna de la memoria
			System.out.print("|");
			System.out.print(SystemMonitor.getDatos(i));
			for (int j = 1; j < (WIDE)-SystemMonitor.getDatos(i).length(); j++) {
				System.out.print(" ");
			}
			System.out.print("|\n");
		}

		for (int i = 0; i <= WIDE; i++) {
			System.out.print("=");
		}
		System.out.println();
		torniquete.release();
		puedesImprimir.release();
	}

	private void clear(){
		System.out.print("\u001b[2J");
		System.out.flush();
	}
}
