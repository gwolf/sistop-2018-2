/* Este programa está diseñado para no hacer nada, y "morirse"
 * lanzando una excepción.
 *
 * El sistema operativo "mata" al proceso en cuestión, produciendo un
 * código de retorno "96".
 *
 * La versión que mostré en clase básicamente no hacía nada más que
 * morirse :-P Decidí hacerlo un poco más "interactivo" para que
 * resulte más claro, más cercano al programita en Python y en Ruby
 * que les presenté.
 *
 * Verán que en el primer caso, para mi gran sorpresa, *funciona* con
 * una semántica muy similar a la que vimos en Ruby. Ya en el segundo caso...
 */
#include <stdio.h>
void main(){
  float i = 10.0, j = 10.0;
  int a = 10, b = 10;

  printf("Ahí vamos con los flotantes. i vale %f, j vale %f.\n", i, j);
  while (i-- > 0) {
    printf("... %f / %f = ", j, i);
    j = j / i;
    printf("%f\n", j);
  }
  printf("Terminamos. i vale %f, j vale %f\n", i, j);

  printf("Ahí vamos con los enteros. a vale %d, b vale %d.\n", a, b);
  while (a-- > 0) {
    printf("... %d / %d = ", a, b);
    b = b / a;
    printf("%d\n", b);
  }
  printf("Terminamos con los enteros. a vale %d, b vale %d.\n", a, b);
}
