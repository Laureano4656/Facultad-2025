; Construir un programa que almacene en un vector los mínimos de cada columna de una matriz 
; de números enteros. 

            MOV EFX,3 //M cols
            MOV EEX,3 //N fils
            MOV EDX,DS
            MOV [EDX],EEX //guardo M en la posicion 0
            ADD EDX,4
            MOV [EDX],EFX //guardo N en la posicion 4
            MOV EFX,0 //contador filas i
            MOV EEX,0 //contador columnas j
carga_Mat:  MOV EDX,DS
            ADD EDX,8 //me muevo a la posicion 8 donde empieza la matriz
            ADD EDX,EFX
            MUL EDX,[4]
            ADD EDX,EEX
            MUL EDX,4 //avanza de a 4 celtas (bytes)
            LDL ECX,1
            LHL ECX,4 
            MOV EAX,1
            SYS 1
            CMP [EDX],0 //SUPONGO CONDICION DE CORTE NUM NEGATIVO
            JN fin_carga // si es negativo, fin

            MOV EFX,0 //contador filas i
            MOV ECX,0 //contador columnas j

genera_v:   CMP ECX,[0] //mientras j < M
            JZ fin // si es j > M, fin
            MOV EBX,9999 //inicializo minimo
fila:       CMP EFX,[4] //mientras i < N
            JZ sig_col // si es i > N, siguiente columna
            MOV EDX,EFX //EDX = i
            MUL EDX,[0] //multiplico i * M
            ADD EDX,ECX //sumo j
            MUL EDX,4 //avanza de a 4 celtas (bytes)
            MOV EDX,DS
            ADD EDX,8 //sumo base de la matriz
            CMP EBX,[EDX] 
            JN nuevo_min // si es menor, nuevo minimo
            JMP sig_fila //sino, siguiente fila

nuevo_min:  MOV EBX,[EDX] // nuevo minimo
sig_fila:   ADD EFX,1 // i++
            JMP fila // repetir
sig_col:    MOV EDX,DS
            ADD EDX,ECX //sumo J
            MUL EDX,4 //avanza de a 4 celtas (bytes)
            ADD EDX,20 //me muevo a la posicion 20 donde empieza el vector
            MOV [EDX],EBX //guardo el minimo en el vector
            ADD ECX,1 // j++
            MOV EFX,0 // reinicio i
            JMP genera_v // repetir








            