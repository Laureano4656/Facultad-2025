#include <string.h>
#include <stdio.h>
#include <stdlib.h>
void fillString(char *s, int nro){
 int i=0;
 int number = nro;
 while (number){
    int bit = number & 0b000000000000001;
    if (bit)
     s[i] = '1';
    else
     s[i] = '0';
    number = number>>1;
    i++;
 }
 printf("\n%X = %s",nro,s);
}

int main(){
 char s[17]="";
 int n;
 scanf("%d",&n);
 fillString(s,n);
 return 0;
}
