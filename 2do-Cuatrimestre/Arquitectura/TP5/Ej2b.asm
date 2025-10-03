SCPY:  PUSH BP
       MOV BP,SP
       PUSH EDX
       MOV EDX,[BP + 8] ; puntero a primer string
       PUSH EAX
       MOV EAX, [BP + 12] ; puntero a segundo string
LOOP:  CMP b[EAX],0 ; comparo con el terminator
       JZ FIN
       MOV b[EDX],b[EAX]
       ADD EDX,1
       ADD EAX,1
       JMP LOOP
FIN:   MOV b[EDX],0
       POP EAX
       POP EDX
       MOV SP,BP
       POP BP
       RET