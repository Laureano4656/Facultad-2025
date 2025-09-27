#include <stdio.h>

void weekDaySet(char *c,int n){
 switch (n){
  case 0:
   *c = *c |0b00000001;
   break;
  case 1:
   *c = *c |0b00000010;
   break;
  case 2:
   *c = *c |0b00000100;
   break;
  case 3:
   *c = *c |0b00001000;
   break;
  case 4:
   *c = *c |0b00010000;
   break;
  case 5:
   *c = *c |0b00100000;
   break;
  case 6:
   *c = *c |0b01000000;
 }
}

void weekDayReset(*char, int n){
switch (n){
  case 0:
   *c = *c & 0b11111110;
   break;
  case 1:
   *c = *c & 0b11111101;
   break;
  case 2:
   *c = *c & 0b11111011;
   break;
  case 3:
   *c = *c & 0b11110111;
   break;
  case 4:
   *c = *c & 0b11101111;
   break;
  case 5:
   *c = *c & 0b11011111;
   break;
  case 6:
   *c = *c & 0b10111111;
 }
}
int main(){
 char c=0b01000000;

 return 0;
}
