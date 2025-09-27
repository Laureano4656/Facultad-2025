#include <stdio.h>
#include <string.h>
void toUpper(char *c){
 int length = strlen(c);
 printf("%d\n",length);
 for (int i=0;i<length;i++){
    printf("c[%d] = %c || c[%d] = %X || c[%d] = %d\n",i,c[i],i,c[i],i,c[i]);
    char test = c[i] & 0x00DF;
    printf("%c\n",test);
    c[i] = test;
 }
 printf("%s",c);
}
int main(){
 char s[] = "Boca";
 toUpper(s);
 return 0;
}
