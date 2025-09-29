; Hacer un programa que permita ingresar una lista de números, que finaliza con un número
; negativo. Luego el programa pedirá ingresar n-1 números de la misma lista, y al finalizar la
; carga deberá mostrar el número que falta de la lista original. Nota: los números de la primera
; lista pueden ser ingresados en cualquier orden. Ejemplo: se ingresan 4,5,3,7,-1 luego 3,7,4 y
; muestra 5.
; a. Resolver el problema a través de un vector.
; b. Proponer una solución sin utilizar arreglos.

        MOV EEX,1 ; EEX = 1
otro:   MOV EDX,DS
        ADD EDX,EEX
        MOV EAX,1
        LDL ECX,0x01
        LDH ECX,0x04
        SYS 1
        CMP [EDX],0
        JN busca
        ADD EEX,1
        JMP otro
        MOV EFX,1 ; EFX = 0
        MOV EBX,EEX
        SUB EBX,1
busca:  MOV EDX,DS
        ADD EDX,EEX
        ADD EDX,EFX
        MOV EAX,1
        LDL ECX,0x01
        LDH ECX,0x04
        SYS 1
        CMP [EDX],[DS+EFX]
        JNZ fin
        ADD EFX,1
        CMP EFX,EBX
        JNZ busca
        