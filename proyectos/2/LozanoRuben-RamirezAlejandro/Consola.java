package proyecto2SisTop;

public class Consola {

	public static void main(String[] args) {
		int a=-1;
		Disco d2=new Disco();
		// TODO Auto-generated method stub
		Disco d1= new Disco();
		Leer l1= new Leer();
		
		System.out.println("unidades");
		do {
			d1.mostrarUnidades();
			a=opcionesUnidad();
			if(a==1)
				d1.crearUnidad(l1.leerUnidad());
			if(a==2)
				d1.borrarUnidad(l1.leerUnidad());
			if(a==3)
				d2=d1;
		}while(a!=3);
		
	}
	public static byte opcionesUnidad() {
		byte a;
		Leer l1= new Leer();
		System.out.println("\n1)agregarUnidad\n2)borrarUnidad\n3)SeleccionarUnidad");
		a=l1.leerOpcUnidad();
		return a;
	}


}
