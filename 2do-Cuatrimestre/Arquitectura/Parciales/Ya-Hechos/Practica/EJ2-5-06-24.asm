; PUSH <fecha nacimiento>
; PUSH <fecha actual>
; CALL ES_MAYOR
; ADD SP,8
; En EAX 1 si es mayor 0 si no es mayor

ES_MAYOR:   PUSH BP
            MOV BP,SP
            PUSH EBX
            PUSH EFX
            MOV EBX, [BP+8] ; fecha actual
            MOV EFX, [BP+12] ; fecha de nacimiento
            SUB EBX, EFX
            SHR EBX, 16 ; obtengo el año
            CMP EBX, 18
            JNN mayor
            MOV EAX,0
            JMP fin_es_mayor
mayor:      MOV EAX,1
fin_es_mayor:   POP EFX
                POP EBX
                MOV SP,BP
                POP BP
                RET

; PUSH <fecha a comprobar>
; PUSH <puntero a lista>
; CALL GET_MAYORES
; ADD SP,8
; En EAX 
GET_MAYORES:    PUSH BP
                MOV BP,SP
                SUB SP,4
                PUSH EBX
                PUSH EDX
                PUSH EFX; celda tipo persona

                MOV [BP-4],null
                MOV EDX,null ; doble puntero a la lista
                MOV EBX, [BP+8] ; puntero simple a lista

otro_get:       CMP EBX, null
                JZ fin
                MOV EFX,[EBX+persona]
                PUSH [EFX+nacimiento]
                PUSH [BP+12]
                CALL ES_MAYOR
                ADD SP,8
                MOV EBX, [EBX+SIG] ; muevo el puntero actual
                CMP EAX,1
                JNZ otro_get
                ADD EFX, nombre
                PUSH EFX
                CALL nnom_create
                ADD SP,4 ;En eax tengo puntero al nuevo nodo
                CMP EDX, null ; reviso si es el primer nodo que inserto
                JNZ insertar
                MOV EDX,BP
                SUB EDX,4 ; tengo mi doble puntero a la lista
insertar:       PUSH EAX
                PUSH EDX
                CALL nnom_add
                ADD SP,4
                ; ya se insertó el nuevo nodo
                JMP otro_get

fin:            MOV EAX, [EDX]
                POP EFX
                POP EDX
                POP EBX
                MOV SP, BP
                POP BP
                RET