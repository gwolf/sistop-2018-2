package tarea3;

public class CeldaMemoria {
	
	int direccion;
	String contenido;
	boolean disponible;
	char disp;
	
	public CeldaMemoria() {
		contenido="***vacio**";
		disponible=true;
		disp='s';
	}
	
	public void setContenido(String algo) {
		this.contenido=("Proceso: "+algo);
		this.disponible=false;
		this.disp='n';
	}

}
