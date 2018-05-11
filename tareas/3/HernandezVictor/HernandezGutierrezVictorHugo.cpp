#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <string.h>
#include <iomanip>
using namespace std;

int main() {

    char cadena[30]={0},SNCa,Proceso,Procesos[26]={0};
    int tam=0,op=0,tamN,i=0;
    char PLiberar;
    Proceso='A';
    do{
    	cout<<"\nAsignar(0) o Liberar(1)): ";
    	cin>>op;
    	if(op==0){//Asignar
    		cout<<"Nuevo proceso ("<<Proceso<<"):";
    		cin>>tamN;
    		cout<<"Nueva Asignacion:"<<endl;

			for(int iEn=tam; iEn<tamN+tam; iEn++){		//agregar los procesos
					cadena[iEn]=Proceso;
			}
			for(int jEn=0; jEn<30; jEn++){		//imprimir procesos asignados
				if (cadena[jEn]!='\0'){					
					cout<<cadena[jEn];
				}else{
					cout<<"-";					
				}	
			}
			Procesos[i++]=Proceso;
    		Proceso++;;
    		tam=tamN+tam;
    	}else if(op==1){//Liberar
    		cout<<"Proceso a liberar ("<<Procesos<<"): ";
    		cin>>PLiberar;
    		for(int iEn=0; iEn<30; iEn++){		//liberar los procesos
				if(cadena[iEn]==PLiberar){
					cadena[iEn]='-';
				}
			}
			for(int jEn=0; jEn<30; jEn++){		//imprimir procesos 
				if (cadena[jEn]!='\0'){					
					cout<<cadena[jEn];
				}else{
					cout<<"-";					
				}	
			}
    	}else{
    		exit(1);
    	}
	}while('null');
}
