#include <stdio.h>

short int codeDate(int month,int day,int year){
 short int dayCoded = (0b000000000011111 & day) << 11;
 short int monthCoded = (0b0000000000001111 & month) <<7;
 short int yearCoded = (0b0000000001111111 & year);

 return (dayCoded | monthCoded) | yearCoded;
}
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
 short int a = codeDate(2,4,70);
 printDate(a);
 return 0;
}
