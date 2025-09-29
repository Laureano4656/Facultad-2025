; 12. Construir un programa que almacene en un vector los mínimos de cada columna de una matriz
; de números enteros.
; Asumo una matriz cargada con la dimesion N en 116 de memoria, la dimesion M en 120 de memoria
; y la matriz a partir de 124 de memoria.

        MOV EFX,0 ; EFX <- J (contador de columnas)
        MOV AC, [116] ; AC <- N
        MUL AC, [120] ; AC <- N * M
        MOV EAX,DS
        ADD EAX,AC ; EAX <- &matriz[N][M]
        ADD EAX,4 ; EAX <- &matriz[N][M] + 4 (siguiente posición para el vector de mínimos)
        MOV EEX,2147483647  ; EEX <- min (mínimo de la columna)
otro:   MOV [EAX],EEX
        ADD EAX,4 ; EAX <- &vector_minimos[J+1]
        MOV ECX,0 ; ECX <- I (contador de filas)
        MOV EEX,2147483647  ; EEX <- min (mínimo de la columna)
        CMP EFX,[120] ; Comparo J con M
        JNZ fin ; Si J >= M, termino
fila:   MOV EDX,120 ; EDX <- M
        MUL EDX,ECX ; EDX <- M * I
        ADD EDX,EFX ; EDX <- M * I + J
        ADD EDX,DS ; EDX <- &matriz[I][J]
        CMP EEX,[EDX] ; Comparo matriz[I][J] con min
        JNN sigue ; Si matriz[I][J] >= min, sigo
        MOV EEX,[EDX] ; min <- matriz[I][J]
sigue:  ADD ECX,1 ; I++
        CMP ECX,[116] ; Comparo I con N
        JNZ fila ; Si I < N, sigo
        ADD EFX,1 ; J++
        JMP otro ; Sigo con la siguiente columna
fin:    MOV AC, [120] ; AC <- M
        MUL AC,4 ; AC <- M * 4 (tamaño del vector de mínimos)
        SUB EAX,AC ; EAX <- &vector_minimos[0]
        MOV EDX,EAX ; EDX <- &vector_minimos[0]
        MOV EAX,1
        LDL ECX,[120]
        LDH ECX,0x04