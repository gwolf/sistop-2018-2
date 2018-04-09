import java.util.ArrayList;
import java.util.concurrent.Semaphore;

//Clase principal.

class SystemMonitor {

	private static Coordinator coordinator = new Coordinator();
	private static ArrayList<String> datos = new ArrayList<String>();

	public static void main(String[] args) {
		coordinator.start();
	}

	public static boolean addDatos(String aux){
		return datos.add(aux);
	}
	public static void clearDatos(){
		datos.clear();
	}
	public static String getDatos(int aux){
		return datos.get(aux);
	}
	public static int sizeDatos(){
		return datos.size();
	}
}
