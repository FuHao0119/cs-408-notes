#include <stdio.h>
int main(){
  unsigned char uc = 8;
  uc = ~uc;
  printf("%d\n",uc);
  return 0;
}
