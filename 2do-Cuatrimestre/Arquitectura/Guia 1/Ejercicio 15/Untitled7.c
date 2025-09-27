#include <stdio.h>

void printDate(unsigned short int x){
 int day = x>>11;
 int month = (x>>7) & 0b0000000000001111;
 int year = x & 0b0000000001111111;
 if (year<50)
  printf("La fecha es: 20%02d-%02d-%02d\n",year,month,day);
 else
  printf("La fecha es: 19%02d-%02d-%02d\n",year,month,day);
}

int main(){
 unsigned short int date = 0b0010000101000110;
 printDate(date);
 return 0;
}
