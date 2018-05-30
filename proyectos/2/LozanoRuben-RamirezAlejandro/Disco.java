
package proyecto2SisTop;
import java.io.*;

public class Disco {
	
	public short tamaño;
	public String[] usuarios= new String[10];
	public String[] unidades = new String[10];
	
	public Disco() {
		this.tamaño=4400;
	}
	
	public void agregarUsuario(String nombre) {
		int a=1,b=0;
		for (int i = 0; i < usuarios.length; i++) {
			if (usuarios[i].indexOf(nombre) != -1) {
				a=0;
				b=i;
			}
		}if (a==0) {
				usuarios[b]=nombre;
			}else {
				System.out.println("ya existe el usuario");
			}
	}

	
	public void reducirTamaño(short tamaño) {
		this.tamaño=(short)(this.tamaño-tamaño);
	}
	public void aumentarTamaño(short tamaño) {
		this.tamaño=(short)(this.tamaño-tamaño);
	}
	public void borrarUnidad(String id) {
		int a=1,b=0;
		for (int i = 0; i < unidades.length; i++) {
			if (unidades[i].equals(id)) {
				a=0;
				b=i;
			}
			
			if (a==0) {
				unidades[b]="\0";
				System.out.println("unidad borrada");
			}else {
				System.out.println("no existe la unidad");
			}
		}
	}
	public void crearUnidad(String id) {
		int a=1,b=0;
		for (int i = 0; i < unidades.length; i++) {
			if (unidades[i].equals(id)) {
				a=0;
				b=i;
			}
		}	
		if (a==0) {
				this.unidades[b]=id;
			}else {
				System.out.println("ya existe la unidad");
			}
	}
	public void mostrarUnidades() {
		for (int i = 0; i < unidades.length; i++) {
			System.out.println("unidad "+i+"="+unidades[i]);
		}
	}
	
}
