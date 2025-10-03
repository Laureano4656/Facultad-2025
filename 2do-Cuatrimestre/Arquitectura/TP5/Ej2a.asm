SLEN:  PUSH BP
       MOV BP, SP
       PUSH EDX ; Guardar EDX
       MOV ECX, 0 ; Inicializar longitud a 0
       MOV EDX, [BP + 8] ; Cargar dirección del string
LOOP:  CMP [EDX + EAX], 0 ; Comparar carácter actual con null terminator
       JZ FIN ; Si es null terminator, fin del string
       ADD ECX, 1 ; Incrementar longitud
       ADD EDX, 1 ; Mover al siguiente carácter
       JMP LOOP
FIN:   POP EDX
       MOV SP,BP
       POP BP
       RET