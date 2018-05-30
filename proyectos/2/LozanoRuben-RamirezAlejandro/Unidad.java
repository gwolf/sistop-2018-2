package proyecto2SisTop;

public class Unidad {
	public int tamaño;
	public String[] directorio= new String[100];
	public char id;
	
	public Unidad(int tamaño) {
		this.tamaño=tamaño;
		this.id='a';
	}
	
	public void agregarADir(String nombre) {
		int a=1,b=0;
		for (int i = 0; i < directorio.length; i++) {
			if (directorio[i].indexOf(nombre) != -1) {
				a=0;
				b=i;
			}
		}if (a==0) {
				directorio[b]=nombre;
				
			}else {
				System.out.println("ya existe el archivo");
			}
	}
	public void borrarDeDir(String nombre) {
		int a=1,b=0;
		for (int i = 0; i < directorio.length; i++) {
			if (directorio[i].indexOf(nombre) != -1) {
				a=0;
				b=i;
			}
		}if (a==0) {
				directorio[b]="\0";
				
			}else {
				System.out.println("ya existe el archivo");
			}
	}
	
}
