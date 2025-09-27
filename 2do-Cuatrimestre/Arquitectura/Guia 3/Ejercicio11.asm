; Desarrollar un algoritmo que permita hallar el valor máximo de un vector de enteros y su
; cantidad de apariciones.

            MOV EFX,0 ; EFX = índice del vector
            MOV EBX,0 //maximo
            MOV EEX,0 //contador de apariciones
inicio:     MOV EDX,DS
            ADD EDX,EFX
            MUL EDX,4
            MOV EAX,1
            LDL ECX,0x01
            LDH ECX,0x04
            SYS 1
            CMP [EDX],0
            JN fin
            ADD EFX,1 ; incremento índice del vector
            CMP EBX,[EDX]
            JN new_max; si el valor actual es mayor que el máximo
            JZ repetido
new_max:   MOV EBX,[EDX] ; actualizo el máximo
           MOV EEX,1 ; reinicio contador de apariciones
           JMP inicio
repetido:  ADD EEX,1 ; incremento contador de apariciones
           JMP inicio
fin:       MOV EDX,DS
           ADD EDX,EFX
           MUL EDX,4
           MOV [EDX],EBX ; guardo el máximo en la última posición del vector
           ADD EDX,4 ; me muevo a la siguiente posición
           MOV [EDX],EEX ; guardo el contador de apariciones
           MOV EAX,1
           LDL ECX,0x02
           LDH ECX,0x04
           SUB EDX,4 ; vuelvo a la posición del máximo
           SYS 2 ; system call para imprimir
           STOP