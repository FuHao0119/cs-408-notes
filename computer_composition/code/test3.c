#include <stdio.h>
int main()
{
  float a = 0.0;
  float b = 0.1;
  for(int i=0; i<100;i++){
    a += b;
  }
  printf("%f\n", a);
  return 0;
}
