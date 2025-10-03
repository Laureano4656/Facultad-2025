SCMP:   PUSH BP
        MOV BP,SP
        PUSH ECX ; PRIMERA CADENA
        PUSH EDX; SEGUNDA CADENA
        MOV ECX,[BP+8] 
        MOV EDX,[BP+12]
        MOV EAX,0 ; en principio son iguales
LOOP:   CMP b[EDX],0
        JZ FIN
        CMP b[ECX],0
        JZ FIN
        
        MOV EAX, b[ECX] ; AL = char1
        SUB EAX,b[EDX] ; AL = char1 - char2
        JNZ FIN

        ADD ECX,1
        ADD EDX,1
        JMP LOOP
FIN:    POP EDX
        POP ECX
        MOV SP,BP
        POP BP
        RET