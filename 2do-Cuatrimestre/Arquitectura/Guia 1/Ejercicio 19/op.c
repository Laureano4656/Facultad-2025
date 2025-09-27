#include <stdio.h>
#include <stdlib.h>
typedef int (*Operacion)(int,int);

int operacionUno(int A,int B){
 return A+B;
}
void operacionDos(int A,int B){
 return A & B;
}
int operacionTres(int A,int B){
 return A;
}
int operacionCuatro(int A,int B){
 return ~A;
}

int main(int argc, char *argv[]){
 if (argc < 3) {
   fprintf(stderr, "Uso: %s <op> <A> [B]\n", argv[0]);
   return 1;
 }
 Operacion test[3] = {operacionUno,operacionDos,operacionTres};
 int op = atoi(argv[1]);
 int A  = atoi(argv[2]);
 int B  = (argc >= 4) ? atoi(argv[3]) : 0;
 int res =  test[op](A,B);
 printf("Resultado = %d\n", res);
 return 0;
}
