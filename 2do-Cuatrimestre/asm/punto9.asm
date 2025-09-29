inicio:     MOV EDX, DS
            ADD EDX, 4
            LDL ECX,4
            LHL ECX,1
            SYS 1
            MOV EEX, [EDX] // cargo el numero de la mascara
read:          mov     eax, 0b01        ; seteo para leer en decimal  
               mov     edx, DS          ; guardar en el data segment 
               add     edx, 4           ; ...en la posición 1 
               ldh     ecx, 0x04        ; leer celdas de 4 bytes 
               ldl     ecx, 0x01        ; leer una sola celda 
               sys     0x1              ; system call para leer 
               Cmp    [edx], 0           ; comparo para validar negativo
               jn       fin  
               xor      ac, ac          ; reseteo el ac (ac = 0) 
               mov     eax, [edx]       ; copio 4 bytes de memoria a registro 
               AND     EAX, EEX        ; APLICAMOS AND 
otro:          cmp     eax, 0           ; comparo con cero 
               jz     show              ; si es cero terminé 
               jp     sigue             ; si no es negativo salta 
               add      ac, 1           ; si es negativo acumula 1 
sigue:         shl     eax, 1           ; desplazo un bit a la izquierda 
               jmp    otro              ; continua el loop 
show:          add     edx, 4           ; incremento para usar otra posición 
               mov   [edx], ac          ; copia a memoria el ac 
               mov     eax, 0b01        ; seteo para escribir decimal 
               ldh     ecx, 0x04        ; escribir celdas de 4 bytes 
               ldl     ecx, 0x01        ; escribir una sola celda 
               sys     0x2              ; system call para imprimir 
               jmp     read

fin:           stop                     ; detener