#include <stdio.h>
int correme() {
  char* buf;
  printf("Dime... ");
  scanf("%s", &buf);
  if (buf[0] == 'H')
    return 0;
  return 1;
}
