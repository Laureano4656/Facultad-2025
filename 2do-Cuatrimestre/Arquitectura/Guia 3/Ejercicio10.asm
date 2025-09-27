; Hacer un programa que permita ingresar una lista de números, que finaliza con un número
; negativo. Luego el programa pedirá ingresar n-1 números de la misma lista, y al finalizar la
; carga deberá mostrar el número que falta de la lista original. Nota: los números de la primera
; lista pueden ser ingresados en cualquier orden. Ejemplo: se ingresan 4,5,3,7,-1 luego 3,7,4 y
; muestra 5.
; a. Resolver el problema a través de un vector.
; b. Proponer una solución sin utilizar arreglos.

            MOV EEX,0 ; EEX = N
            MOV EBX,0 ; acumulador de lista 1
otro:       MOV EDX,DS
            ADD EDX,EEX
            MUL EDX,4
            MOV EAX,1
            LDL ECX,0x01
            LDH ECX,0x04
            SYS 1
            CMP [EDX],0
            JN sigue
            ADD EBX,[EDX]
            ADD EEX,1
            JMP otro
sigue:      MOV EFX,1 ; EFX = indice para recorrer n-1 veces
            ; MOV EBX,EEX; guardo n-1 en EBX
            ; SUB EBX,1
            MOV AC,0
seg_lista:  MOV EDX,DS
            ADD EDX,EEX
            ADD EDX,EFX
            MUL EDX,4
            MOV EAX,1
            LDL ECX,0x01
            LDH ECX,0x04
            SYS 1        
            ADD EFX,1
            ADD AC,[EDX]
            CMP EFX,EEX
            JNZ seg_lista
            SUB EBX,AC
            MOV EDX,DS
            MOV [EDX],EBX
            MOV EAX,0x01
            LDL ECX,0x04
            LDH ECX,0x01
            SYS 0x2
            STOP
