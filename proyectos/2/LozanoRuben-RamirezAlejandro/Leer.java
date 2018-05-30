package proyecto2SisTop;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Leer {
	public byte leerOpcUnidad() {
		byte numero = 0;
		boolean estado=true;
		
			InputStreamReader letra= new InputStreamReader(System.in);
			BufferedReader renglon = new BufferedReader(letra);
		while(estado) {	
			try {
				System.out.println("ingrese una opcion ");
				numero= Byte.parseByte(renglon.readLine());
				if(numero<4 && numero>0)
					estado=false;
				else
					System.out.println("instruccion no identificada");
				
			}catch(IOException entrada) {
				System.out.println("Falla al leer del teclado: "+ entrada.getMessage());
			}
			catch(NumberFormatException convierte) {
				System.out.println("\nFalla al convertir la cadena a numero: "+convierte.getMessage());
			}
		}
		return numero; 
		
	}	
	public String leerUnidad() {
		String cadena="/0";
		boolean estado=true;

			InputStreamReader letra= new InputStreamReader(System.in);
			BufferedReader renglon = new BufferedReader(letra);
		while(estado) {
			try {
				System.out.println("ingrese una letra para identificar a la unidad");
				cadena= renglon.readLine();
				if(cadena.length()==1)
					estado=false;
				else
					System.out.println("utilice una letra solamente");
				
			}catch(IOException entrada) {
				System.out.println("Falla al leer del teclado: "+ entrada.getMessage());
			}
	}

		
		return cadena; 
		
	}
	
	
	public byte leerByte() {
		byte numero = 0;
		boolean estado=true;
		
			InputStreamReader letra= new InputStreamReader(System.in);
			BufferedReader renglon = new BufferedReader(letra);
		while(estado) {	
			try {
				System.out.println("aqui va el mensaje ");
				numero= Byte.parseByte(renglon.readLine());
				estado=false;
				
			}catch(IOException entrada) {
				System.out.println("Falla al leer del teclado: "+ entrada.getMessage());
			}
			catch(NumberFormatException convierte) {
				System.out.println("\nFalla al convertir la cadena a numero: "+convierte.getMessage());
			}
		}
		return numero; 
		
	}	
	public boolean leerBoolean() {
		String cadena= "\0";
		boolean estado=true,resultado=true;
		
			InputStreamReader letra= new InputStreamReader(System.in);
			BufferedReader renglon = new BufferedReader(letra);
		while(estado) {	
			try {

				cadena=renglon.readLine();
				if(cadena=="si") {
					estado=false;
					resultado=true;
				}	
				if(cadena=="no") {
					estado=false;
					resultado=false;
				}
			}catch(IOException entrada) {
				System.out.println("Falla al leer del teclado: "+ entrada.getMessage());
			}
			catch(NumberFormatException convierte) {
				System.out.println("\nFalla al convertir la cadena a numero: "+convierte.getMessage());
			}
		}
		return resultado; 
		
	}
	
	public  float leerFloat() {
		float numero = 0f;
		boolean estado=true;
		
			InputStreamReader letra= new InputStreamReader(System.in);
			BufferedReader renglon = new BufferedReader(letra);
		while(estado) {	
			try {
				
				numero= Float.parseFloat(renglon.readLine());
				estado=false;
				
			}catch(IOException entrada) {
				System.out.println("Falla al leer del teclado: "+ entrada.getMessage());
			}
			catch(NumberFormatException convierte) {
				System.out.println("\nFalla al convertir la cadena a numero: "+convierte.getMessage());
			}
		}
		return numero; 
		
	}
	
	public  short leerShort() {
		short numero = 0;
		boolean estado=true;
		
			InputStreamReader letra= new InputStreamReader(System.in);
			BufferedReader renglon = new BufferedReader(letra);
		while(estado) {	
			try {
				
				numero= Short.parseShort(renglon.readLine());
				estado=false;
				
			}catch(IOException entrada) {
				System.out.println("Falla al leer del teclado: "+ entrada.getMessage());
			}
			catch(NumberFormatException convierte) {
				System.out.println("\nFalla al convertir la cadena a numero: "+convierte.getMessage());
			}
		}
		return numero; 
		
	}
	
	public String leerCadena() {
		String cadena="/0";

			InputStreamReader letra= new InputStreamReader(System.in);
			BufferedReader renglon = new BufferedReader(letra);
		
			try {
				System.out.println("aqui va el mensaje ");
				cadena= renglon.readLine();
		
				
			}catch(IOException entrada) {
				System.out.println("Falla al leer del teclado: "+ entrada.getMessage());
			}

		
		return cadena; 
		
	}
}
