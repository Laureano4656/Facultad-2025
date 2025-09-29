// Hacer un programa que permita ingresar una lista de números, que finaliza con un número 
// negativo. Luego el programa pedirá ingresar n-1 números de la misma lista, y al finalizar la 
// carga deberá mostrar el número que falta de la lista original. Nota: los números de la primera 
// lista pueden ser ingresados en cualquier orden. Ejemplo: se ingresan 4,5,3,7,-1 luego 3,7,4 y 
// muestra 5.  
  
            MOV EEX,0 //n del vector
inicio:     MOV EDX, DS
            ADD EDX,EEX
            MUL EDX,4 //avanza de a 4 celtas (bytes)
            LDL ECX,1
            LHL ECX,4 
            MOV EAX,1
            SYS 1
            COMP [EDX],0 
            JN sigue // si es negativo, siguiente ciclo
            ADD EBX,[EDX] // suma todos los numeros
            ADD EEX,1 //n++
            JMP inicio // repetir

sigue:      MOV EFX,1//contador de n-1, arranco en 1
seg_lista:  MOV EDX,DS
            ADD EDX,EEX
            ADD EDX,EFX
            MUL EDX,4  
            LDL ECX,1
            LHL ECX,4
            MOV EAX,1
            SYS 1
            ADD EFX,1 //contador++
            ADD AC,[EDX] //acumulo los numeros ingresados
            CMP EFX,EEX
            JNZ seg_lista //mientras no llegue a n, sigo

busca:      SUB EBX,AC //resto la suma de los n-1 a la suma de los n
            MOV EDX,DS
            MOV [EDX],EBX
            LDL ECX,1
            LHL ECX,4
            MOV EAX,1
            SYS 2
            STOP
            


