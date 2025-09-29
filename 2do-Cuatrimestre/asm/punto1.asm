inicio:	XOR AC,AC // contador
	    MOV EFX,0 // suma
otro:	MOV EDX,DS // buffer
	    LDL ECX,0x04 // size
	    LDH ECX,0x01 // read
	    MOV EAX,0x01 //read
	    SYS 1
	    COMP EDX,0 // fin de archivo
        JN fin // si es negativo, fin
        ADD AC,1 // contador++
        ADD EFX,[EDX] // suma += valor
        JMP otro // repetir
fin:	DIV EFX,AC // promedio = suma / contador
        MOV [0],EFX // guardar promedio en memoria
        MOV EDX,0 // buffer
        LDL ECX,0x04  // size
        LHL ECX,0x01 // write
        SYS 2 // write
        stop // detener
	