#include <stdio.h>

void weekDays(char c){
 int i=0;
 char bits=c;
 printf("%04X\n",c);
 while (bits){
    int bit = (int)bits & 0b00000001;

    if (bit){
        switch (i){
         case 0:
          printf("Domingo\n");
          break;
         case 1:
          printf("Lunes\n");
          break;
         case 2:
          printf("Martes\n");
          break;
         case 3:
          printf("Miercoles\n");
          break;
         case 4:
          printf("Jueves\n");
          break;
         case 5:
          printf("Viernes\n");
          break;
         case 6:
          printf("Sabado\n");
        }
    }
    i++;
    bits = bits>>1;
 }
}

int main(){
 weekDays(0b01100000);
 return 0;
}
