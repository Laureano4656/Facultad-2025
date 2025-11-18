_order_list:    PUSH BP
                MOV BP,SP
                PUSH EDX
                PUSH EBX
                MOV EDX,[BP+8] ; puntero doble a lista destino
                MOV EBX,[BP+12] ; puntero simple

                CMP EBX,null
                JZ fin_order
                PUSH [EBX+sig]
                PUSH EDX
                CALL _order_list
                ADD SP,8

                PUSH EBX ;nodo a insertar
                PUSH EDX ; **h
                CALL insert_ordenado
                ADD SP,8

                MOV [EBX+sig], null

fin_order:      POP EBX
                POP EDX
                MOV SP,BP
                POP BP
                RET



order_list:     PUSH BP
                MOV BP,SP
                SUB SP,4
                PUSH EAX

                MOV EAX,BP
                SUB EAX,4
                MOV [EAX],null

                MOV EAX,[BP+8] ; puntero doble lista vieja
                PUSH [EAX]
                MOV EAX,BP
                SUB EAX,4
                PUSH EAX
                CALL _order_list
                ADD SP,8

                MOV EAX,[BP+8]
                MOV [EAX],[BP-4]

                POP EAX
                ADD SP,4
                MOV SP,BP
                POP BP
                RET