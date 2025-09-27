; LEER [0]
; RESULTADO [4]
; EFX va a guardar el contador


            ; Leo el numero que esta en la posicion 0 de memoria
            MOV [4], 0 ; Asumo que no es primo
            MOV EFX, 2
            MOV EDX, DS
            LDL ECX, 1
            LDH ECX, 4
            MOV EAX, 0x01
            SYS 1

            ; Si es 2 cuenta como primo
            CMP [EDX], 2
            JZ FIN

OTRO:       CMP [EDX], EFX ; Resto el numero con el contador
            JNP FIN ; Si hice n - n es porque ya no hay numeros para probar
            DIV [EDX], EFX
            CMP AC, 0 ; Si el resto de hacer la division da 0 (Se guarda en AC) encontre un divisor, termino
            JZ NO_PRIMO
            ADD EFX, 1
            JMP OTRO

FIN:        MOV [4], 1
NO_PRIMO:   MOV [4], 0