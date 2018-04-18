#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>

void main() {
  int *ptr;
  printf("Solicitamos asignaciones del tamaño de un entero es: %d\n", sizeof(int));
  while (1) {
    ptr = malloc(sizeof(int));
    /* usleep se "duerme" por la cantidad de milisegundos especificada: */
    /* Un segundo. */
    usleep(1000);
  }
}
