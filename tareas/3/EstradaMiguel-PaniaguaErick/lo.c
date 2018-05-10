#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main(void)
{
    int x,y,i,cant=4,tam=1,espacios=0,p;
    char *arreglo[cant];
    char *dato;
    char *m;
    char *z;
    
   
printf("\n\n\t\t\t\tBienvenido \n");
printf("\n Pulse enter para iniciar ");
/*Ciclo que permite ingresar las letras de los procesos elemnto a elemnto*/
    for(i=0; i<cant; i++){
        getchar();
        printf("\nIngrese la letra de su proceso: \nlocalidad de memoria en donde se guradara[%i]: ",i);
        /*apuntador a los datos que se van  guardar*/
        dato = (char*) malloc(tam);
        scanf("%[^\n]",dato);
        /*Asignacion de caracter para los espacios libres*/
        if (*dato == ' ') *dato = '-';
        /*Se guarda la variable dato en la localidad de memoria que le corresponde*/
        arreglo[i] = dato;
    }
    free (arreglo[cant]);
    /*Se imprimen el "mapa de memoria" y sus procesos ingresados*/
    printf("\nLos procesos ingresados son: \n");
    for(i=0; i<cant; i++){
        printf("%s",arreglo[i]);
           }      
    getchar();
    getchar();
/*Se inicia el menu*/
    do{
        system("clear");
    printf("Si desea salir del programa [3]\n");
    printf("\nDesea asignar proceso [1] o Liberar proceso [2]: ");
    scanf("%d", &x);
/*Asigancion de operaciones a realizar para cada caso*/
    switch(x)

   {
    /*Contador para el numero de espacios vacios*/
        case 1:
        for(i=0; i<cant; i++){
        if (*arreglo[i] == '-')
            espacios++;
    }
//printf("%d", espacios);
    /*Condicion que permite la asignacion de muevos procesos siguiendo el tamaño preestablecido*/
if (espacios!=1){
        printf("\nIngresar letra de nuevo proceso: ");
        /*Apuntador a la variable del nuevo proceso*/
        m = (char*) malloc(tam);
         scanf("%s",m);
        printf("\nIngresar tamaño del proceso: ");
                scanf("%d",&p);
                    if(p>15) printf("\t\tMaximo de memoria para un proceso: 15");
                else{
                  /*Asignacion del nuevo proceso a las localidades del arreglo que estan vacias*/
             for(i=0; i<cant; i++){
                if(*arreglo[i] == '-') *arreglo[i] = *m;
                  }
            printf("\nEl proceso: [ %s ] se asigno en las localidades de memoria vacia.\n", m);
            printf("\n");
            /*Se imprime el nuevo estado de la memoria de procesos*/
         for(i=0; i<cant; i++){
          printf("%s",arreglo[i]);
    }   
  }
}
        /*Condicion que permite al usuario conocer que se debe liberar memoria*/
        else
            printf(" Liberar memoria por favor. Minimo de memoria para un proceso: 2 ");      
        
    free (arreglo[cant]);
    espacios=0;
    getchar();
       break;

       case 2:
        /*Operaciones que me permiten liberar cierto proceso*/
        printf("\nProceso a liberar: ");
        /*Apuntador al nuevo proceso*/
        z = (char*) malloc(tam);
        scanf("%s",z);
        /*Ciclo que permite liberar el proceso solisitado*/
        for(i=0; i<cant; i++){
          /*Condicion que me permite liberar un proceso existente*/
        if (*arreglo[i] != *z) printf("");
        else 
             {
              /*Condicion que permite liberar el prceso solicitado*/
            if (*arreglo[i] == *z) *arreglo[i] = '-'; 
     printf("\nproceso: [ %s ] liberado\n", z);
         printf("\n");
         /*Ciclo que muestra el nuevo estado de la memoria*/
         for(i=0; i<cant; i++){
          printf("%s",arreglo[i]);
          
} 
}  
}     
    free (arreglo[cant]);
    getchar();
    break;

    case 3:/*Permite salir del programa*/
            exit(0);
            break;
            /*Cualquier otro caso que no este dentro del menu, 
            sera desplegada la siguiente informacion*/
       default: system("clear");
                printf("ahorita no joven\n");
                getchar();
                
    }
    getchar();     
}
/*fin del cilo */
    while(x !=0);
    printf("\n\n");
    return 0;
}    
