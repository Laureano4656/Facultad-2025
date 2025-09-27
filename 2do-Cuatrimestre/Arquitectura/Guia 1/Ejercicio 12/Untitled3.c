#include <stdio.h>

int main(void) {
    int x = -1;
    printf("Entero -1 en memoria (hex): %08X\n", x);
    if (x == ~0) {
        printf("La PC utiliza complemento a 2 para representar negativos.\n");
    } else {
        printf("La PC NO utiliza complemento a 2.\n");
    }

    return 0;
}
