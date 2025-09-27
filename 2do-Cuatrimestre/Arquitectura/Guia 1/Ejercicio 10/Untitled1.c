#include <stdio.h>


int main(){
 int n = 0xA1F8;
 printf("A: %X\n",(n>>8)&0x00FF);
 printf("B: %X\n",(n&0x00FF));
 printf("C: %X\n",n&0x0001);
 printf("D: %X\n",(n&0x8000) ? 0xFFFF : 0x0000);
 printf("E: %X\n",(n>>4)&0x0FFF);
 printf("F: %X\n",n&0x000F);
 return 0;
}
