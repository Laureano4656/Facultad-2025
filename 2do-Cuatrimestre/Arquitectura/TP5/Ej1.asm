POTENCIA:   PUSH BP
            MOV BP, SP
            SUB SP, 4; Reservar espacio para resultado
            PUSH ECX ; Guardar antiguo valor de ecx            
            MOV ECX, [BP + 8] ; Exponente
            MOV [BP - 4], 1 ; Inicializar resultado a 1
LOOP:       CMP ECX, 0
            JZ FIN ; Si exponente es 0, resultado es 1
            MUL [BP - 4], [BP + 4] ; resultado *= base
            SUB ECX, 1
            JMP LOOP
FIN:        POP ECX ; Restaurar exponente
            MOV EAX, [BP - 4] ; Mover resultado a EAX
            MOV SP, BP
            POP BP
            RET 
