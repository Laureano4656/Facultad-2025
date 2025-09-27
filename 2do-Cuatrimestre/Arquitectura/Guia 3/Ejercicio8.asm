read: 
    MOV EAX, 0b01 ; seteo para leer en decimal
    MOV EDX, DS ; guardar en el data segment
    ADD EDX, 4 ; ...en la posición 1
    LDH ECX, 0x04 ; leer celdas de 4 bytes
    LDL ECX, 0x01 ; leer una sola celda
    SYS 0x1 ; system call para leer
    CMP [EDX], 0
    JN fin
    XOR AC, AC ; reseteo el ac (ac = 0)
    MOV EAX, [EDX] ; copio 4 bytes de memoria a registro
otro:
    CMP EAX, 0 ; comparo con cero
    JZ show_bits ; si es cero terminé
    JNN sigue ; si no es negativo salta
    ADD AC, 1 ; si es negativo acumula 1
sigue:
    SHL EAX, 1 ; desplazo un bit a la izquierda
    JMP otro ; continua el loop
show_bits:
    ADD EDX, 4 ; incremento para usar otra posición
    MOV [EDX], AC ; copia a memoria el ac
    MOV EAX, 0b01 ; seteo para escribir decimal
    LDH ECX, 0x04 ; escribir celdas de 4 bytes
    LDL ECX, 0x01 ; escribir una sola celda
    SYS 0x2 ; system call para imprimir
    JMP read
fin:
    STOP