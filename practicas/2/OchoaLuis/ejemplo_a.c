#include <stdio.h>
#include <unistd.h>

int main ()
{

int a = 100; int b = 2;  int result;
result = a- b;
printf("%i\n",result);

 printf("My process ID : %d\n", getpid());
 printf("My parent's ID: %d\n", getppid());
return 0;
}