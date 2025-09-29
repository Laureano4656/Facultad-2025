inicio: mov efx, 0  
        mov ac, -1 // contador de bits
otro:	mov eax, 0b01
        mov edx, ds // buffer
        ldl ecx, 0x04 // size
        lhl ecx, 0x01   // read
        sys 1 // leo
        comp [edx], 0 // comparo con fin de archivo
        jz sigue // si es cero, sigo
        comp [edx], 1 // comparo con 1
        jnz fin // si no es 1, fin
sigue: 	add ac,1  // acumulo cantidad de bits ingresados
        shl [edx], ac //shifteo a izq la cantidad actual de bits
        or efx, [edx] // acumulo el bit en el lugar correspondiente
        jmp otro // repito
fin:	mov edx, efx // buffer
        ldl ecx, 1 // size
        lhl ecx, 4 // write
        mov eax, 0x01 // write
        sys 2 // escribo
        stop // detener
	