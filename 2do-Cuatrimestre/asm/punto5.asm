
inicio: MOV EFX, 0
        MOV EDX, DS
        LDL ECX, 4
        LHL ECX, 1
        MOV EAX, 1
        SYS 1
        MOV EFX, [EDX] //cargo la base
        MOV EBX, [EDX] //guardo la base
        MOV AC,[EFX] //cargo el exponente
        
        CMP EFX,0 //si el exponente es 0
        JNZ f_loop //sino, hago el loop
        MOV EFX,1 //cualquier numero elevado a 0 es 1
        JMP fin  //salto a fin
f_loop:  CMP AC,0 //si el exponente es 0
        JZ fin //si es 0, termino
        SUB AC,1 //resto 1 al exponente
        MOV EEX,AC     //guardo el exponente en EEX
mult_loop:  CMP EEX,0 //mientras el exponente sea distinto de 0
        JZ f_loop //si es 0, termino
        ADD EFX, EBX //sumo la base
        SUB EEX,1 //resto 1 al exponente
        JMP mult_loop //repito

fin:   MOV EDX,DS 
       MOV [EDX],EFX
       LDL ECX,4
       LHL ECX,1
       MOV EAX,1
       SYS 2
       STOP




