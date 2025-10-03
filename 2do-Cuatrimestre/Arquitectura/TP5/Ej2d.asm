SCAT:   PUSH BP
        MOV BP,SP
        PUSH EAX
        PUSH EDX
        MOV EAX, [BP+8]
        MOV EDX, [BP+12]
LOOP1:  CMP b[EAX],0
        JZ LOOP2
        ADD EAX,1
        JMP LOOP1
LOOP2:  CMP b[EDX],0
        JZ FIN
        MOV b[EAX],b[EDX]
        ADD EAX,1
        ADD EDX,1
        JMP LOOP2
FIN:    MOV b[EAX],0
        POP EDX
        POP EAX
        MOV SP,BP
        POP BP
        RET