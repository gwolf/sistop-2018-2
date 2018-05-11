/*
 * INTEGRANTES:
 * Ramirez Gonzalez Jesus Alejandro
 * Lozano Estrada Ruben Omar
 * 
 *  
 * las solicitudes son resueltas por primer ajuste
 * 
 * */
package tarea3;
import java.util.Scanner;
  
public class AsignacionMemoria {

	//main
	public static void main(String[] args) {

		CeldaMemoria pilaMemoria[]=new CeldaMemoria[30];
		String listaProcesos[]=new String[15];
		//metodo que controla el programa
		consola(pilaMemoria);
		
		}
	
	//metodo para mostrar la pila de memoria con formato
	public static void mostrar(CeldaMemoria arreglo[]) {
		
		for (int i = 0; i < 30; i++) {
			if(i==0) {
			
				System.out.printf("_________________________\n");
				System.out.println("|direc.|S/N|   datos    |");
				System.out.printf("-------------------------\n");
				
			}
			System.out.printf("| %4d |%3c| %10s |\n",arreglo[i].direccion,arreglo[i].disp,arreglo[i].contenido);
			
			if(i==29) {
				System.out.printf("-----------------------\n");
			}
				
			
			
			
		}
		//muestra al final la informacion general de la pila de memoria
		infoMemoria(arreglo);
	}
	//inicializa la pila de memoria
	public static void iniciarMemoria(CeldaMemoria arreglo[]) {
		//int numero = (int) (Math.random() * 2000) + 1;//si se activa esta linea y se suma a la linea 51 se pueden obtener direcciones aleatorias
		for (int j = 0; j < arreglo.length; j++) {
			arreglo[j]=new CeldaMemoria();
			arreglo[j].direccion=j*4;
			
		}
	}
	//calcula el espacio disponible: total y contiguo ademas de la direccion de memoria del espacio contiguo
	public static int[] calcularEspacioLibre(CeldaMemoria arreglo[]) {
		int libreContiguo=0;
		int libreContiguoAux[]=new int[3];
		libreContiguoAux[0]=0;
		libreContiguoAux[1]=0;
		libreContiguoAux[2]=0;
		for (int i = 0; i < 30; i++) {
			if((arreglo[i].disponible==true)) {
				libreContiguo+=1;
				libreContiguoAux[2]+=1;//tamañoTotal
				if (libreContiguo>=libreContiguoAux[0]) {
					libreContiguoAux[0]=libreContiguo;//tamañoContiguo
					libreContiguoAux[1]=(i+1)-libreContiguo;//direccion
					
				}
			}
			if(arreglo[i].disponible==false) {
				libreContiguo=0;
			}
		}
		//devuelve el arreglo con la informacion de la memoria
		return libreContiguoAux;
	}
	
	//imprime la informacion de la memoria obtenida con el metodo calcularEspacioLibre()
	public static void infoMemoria(CeldaMemoria arreglo[]) {
		int a[]=new int[3];
		a=calcularEspacioLibre(arreglo);
		System.out.println("memoria contigua disponible:"+a[0]+"direccion donde empieza:"+arreglo[a[1]].direccion+"memoria total disponible:"+a[2]);
	}
	//verifica que lo ingresado por teclado sea una letra
	public static String leerLetra() {
        String entradaTeclado = "";
      
        do {
        	do {
        		System.out.println("ingrese una letra(identificador de proceso):");
            	Scanner entradaEscaner = new Scanner (System.in); 

                entradaTeclado = entradaEscaner.next (); 
        	}while(entradaTeclado.length()>1);
        	//comparacion ascci
        }while(!((((entradaTeclado.codePointAt(0))>=65)&&((entradaTeclado.codePointAt(0))<=90))||(((entradaTeclado.codePointAt(0))>=97)&&((entradaTeclado.codePointAt(0))<=122))));
	     
        System.out.println ("Entrada recibida por teclado es: \"" + entradaTeclado +"\"");
		return entradaTeclado;
	}
	//asigna memoria de la pila a un proceso y en caso de ser necesario compacta la memoria
	public static void asignarMemoriaProceso(CeldaMemoria arreglo[],String a,int cantidad) {
		int libre[]=new int[3];
		int b[]=new int[3];
			b=calcularEspacioLibre(arreglo);
		libre[0]=b[0];//tamaño contiguo
		libre[1]=b[1];//direccion
		libre[2]=b[2];//memoria total
		if(cantidad<=libre[0]&&libre[2]!=0) {
			for (int i = libre[1]; i < (cantidad+libre[1]); i++) {
				arreglo[i].setContenido(a);
				
			}	
		}else {
			//compactacion de la pila
			if (cantidad<=libre[2]&&libre[2]!=0) {
				compactar(arreglo);
				b=calcularEspacioLibre(arreglo);
				libre[0]=b[0];//tamaño contiguo
				libre[1]=b[1];//direccion
				libre[2]=b[2];//memoria total
				for (int i = libre[1]; i < (cantidad+libre[1]); i++) {
					arreglo[i].setContenido(a);
				}
			}else {
				if(libre[2]==0) {
					System.out.println("no hay memoria para asiganr");
				}
			}
		}
	}
	//libera la memoria de un proceso 
	public static void liberarMemoriaProceso(CeldaMemoria arreglo[],String a){
		System.out.println("iniciando liberacion");
		String b="Proceso: "+a;
		for (int i = 0; i < 30; i++) {
			if (0==(arreglo[i].contenido.compareTo(b))) {
				arreglo[i].contenido="***vacio**";
				arreglo[i].disp='s';
				arreglo[i].disponible=true;
				System.out.println("liberando.....");
			}
		}
	}
	//verifica que la entrada del teclado sea un comando valido
	public static String leerComando() {
        String entradaTeclado = "";
        
	        do {
	        	do {
    		
	        		System.out.print("ingrese un comando para utilizar(0:asignar,1:liberar,2:ayuda,3:salir): ");
	            	Scanner entradaEscaner = new Scanner (System.in); //Creación de un objeto Scanner
	
	                entradaTeclado = entradaEscaner.next (); //Invocamos un método sobre un objeto Scanner

	        	}while((entradaTeclado.length()>1)||(entradaTeclado.compareTo("2")==0));
        	//comparacion de numeros
	        }while(!((((entradaTeclado.codePointAt(0))>=48)&&((entradaTeclado.codePointAt(0))<=51))));
		
	        System.out.println ("Comando tecleado es: \"" + entradaTeclado +"\"");
			return entradaTeclado;
	}
	//consola para controlar el proceso de asignacion
	public static void consola(CeldaMemoria memoria[]) {
		String a;
		String opcion;
		iniciarMemoria(memoria);
		
		do {
			mostrar(memoria);
			opcion=leerComando();
			
			if((opcion.compareTo("0"))==0){
				a=letrasDisponibles(memoria);
				asignarMemoriaProceso(memoria,a,leerNumero(memoria));
			}
			if ((opcion.compareTo("1"))==0) {
				System.out.println("ingrese el identificador del proceso que desea liberar");
				a=letrasOcupadas(memoria);
				liberarMemoriaProceso(memoria,a);
			}
			if ((opcion.compareTo("2"))==0) {
				System.out.println("0)asigna memoria a un proceso a peticion del usuario\n1)libera la memoria asignada a un proceso\n2)muestra la informacion de los comandos disponibles\n3)salir");
			}	
		}while(opcion.compareTo("3")!=0);
	}
	//verifica que lo ingresado por consola sea un numero y si hay memoria igual a este en caso negativo mostrara "no hay espacio"
	public static int leerNumero(CeldaMemoria arreglo[]) {
        String entradaTeclado = "";
        
    	do {
	        do {
	        	do {
	        		System.out.println("ingrese la cantidad de memoria que desea asignar(asignacion minima 2)");
	            	Scanner entradaEscaner = new Scanner (System.in); //Creación de un objeto Scanner
	
	                entradaTeclado = entradaEscaner.next (); //Invocamos un método sobre un objeto Scanner
	                
	        	}while( (entradaTeclado.length()>2) );
	        	
	        }while(!((((entradaTeclado.codePointAt(0))>=48)&&((entradaTeclado.codePointAt(0))<=57))||(((entradaTeclado.codePointAt(1))>=48)&&((entradaTeclado.codePointAt(1))<=57))));
	        if((Integer.parseInt(entradaTeclado))>calcularEspacioLibre(arreglo)[2]||calcularEspacioLibre(arreglo)[2]==0) { 
	        	System.out.println("No hay espacio suficiente");
	        }
	        System.out.println ("Cantidad de memoria solicitada es: \"" + entradaTeclado);
    	}while((Integer.parseInt(entradaTeclado) <2));
    	
		return Integer.parseInt(entradaTeclado);
	}
	//analiza que letras estan disponibles para los procesos entrantes
	public static String letrasDisponibles(CeldaMemoria arreglo[]) {
		String a,b;
		int c;
		boolean llave;
		do {
			llave=false;
			System.out.println("1");
			b=leerLetra();
			System.out.println("2");
			a=("Proceso: "+b);
			c=0;
			for (int i = 0; i < arreglo.length; i++) {
				
				if((a.compareTo(arreglo[i].contenido))==0&&c==0) {
					System.out.println("3");
					llave=true;
					c+=1;
					System.out.println("indentificador en uso, ingrese uno nuevo:");
				}
			}
		} while(llave);
		System.out.println("4");
		return b;
	}
	//analiza que letras existen en la memoria para liberarla
	public static String letrasOcupadas(CeldaMemoria arreglo[]) {
		String a,b;
		boolean llave=true;
		do {
			int conteo=0;
			b=leerLetra();
			a=("Proceso: "+b);
			for (int i = 0; i < arreglo.length; i++) {
				
				if((a.compareTo(arreglo[i].contenido))==0) {
					llave=false;
					
				}else {
					conteo+=1;
				}
			}
			if(conteo==30) {
				System.out.println("ese proceso no esta en memoria");
			}
		} while(llave);
		return b;
	}
	//compacta la memoria para tener un espacio contiguo mas grande
	public static void compactar(CeldaMemoria arreglo[]) {
		int vacio=0;
		int k=0;
		System.out.println("iniciando compactacion");
		for (int i = 0; i < arreglo.length; i++) {
			if(arreglo[i].disponible==true){
				vacio+=1;
			}
			if (vacio>0 && arreglo[i].disponible==false) {
				k=i;
				for (int j = k; j < arreglo.length; j++) {
					arreglo[j-vacio]=arreglo[j];
				}
				vacio=0;
				
			}			
		}
		System.out.println("fin compactacion");
		mostrar(arreglo);
	}
}
