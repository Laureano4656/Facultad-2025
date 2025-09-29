; Desarrollar un algoritmo que permita hallar el valor máximo de un vector de enteros y su 
; cantidad de apariciones.

            MOV EFX,0 //n
            MOV EBX,0 //maximo
            MOV EEX,0 //contador de apariciones
inicio:     MOV EDX,DS
            ADD EDX,EFX
            MUL EDX,4 //avanza de a 4 celtas (bytes)
            LDL ECX,1
            LHL ECX,4
            MOV EAX,1
            SYS 1
            ADD EFX,1 //n++
            CMP EDX, 0 //SUPONGO CONDICION DE CORTE NUM NEGATIVO
            JN fin // si es negativo, fin
            CMP EBX,[EDX]
            JN new_max // si es mayor, nuevo maximo
            JZ repe // si es igual, contador++

new_max:    MOV EBX,EDX // nuevo maximo
            MOV EEX,0// reinicio contado
repe:       ADD EEX,1 // contador++
            JMP inicio // repetir

fin:       MOV EDX,DS
           ADD EDX,EFX
           MUL EDX,4
           MOV [EDX],EBX ; guardo el máximo en la última posición del vector
           ADD EDX,4 ; me muevo a la siguiente posición
           MOV [EDX],EEX ; guardo el contador de apariciones
           SUB EDX,4 ; vuelvo a la posición del máximo    
           MOV EAX,1
           LDL ECX,0x02
           LDH ECX,0x04
           SYS 2 ; system call para imprimir
           STOP