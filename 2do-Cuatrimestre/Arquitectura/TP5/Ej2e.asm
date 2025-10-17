SPLIT:  PUSH BP
        MOV BP,SP
        PUSH EDX ; Puntero a string
        PUSH EAX ; caracter
        PUSH ECX ;Puntero a array de punteros
        MOV EDX, [BP + 8]
        MOV AL, [BP + 12]
        MOV ECX, [BP + 16]
        MOV [ECX], EDX ; Cargo la primera posicion de ECX con el inicio del string
LOOP:   CMP b[EDX], 0 ; Comparo con el terminator
        JZ FIN
        CMP b[EDX], AL 
        JNZ OTRO
        MOV [EDX], 0 ; Remplazo el caracter por el terminator
        ADD ECX, 4
OTRO:   ADD EDX,1
        MOV [ECX],EDX ; Muchas veces pisa el mismo valor
        JMP LOOP
FIN:    ADD ECX,4
        MOV [ECX],-1
        POP ECX
        POP EAX
        POP EDX
        MOV SP,BP
        POP BP

