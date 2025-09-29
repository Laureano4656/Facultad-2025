ej resuelto en clase
leer: [0]=[DS] 
resultado: [4] 

	MOV [4],0 // inicializo resultado en 0
inicio: MOV EDX,DS // buffer
	LDL ECX,1 // size
	LHL ECX,4
	MOV EAX,1
	SYS 1 // leo
	COMP [EDX],0 // comparo con fin de archivo
	JZ sigue // si es cero, sigo
	COMP [EDX],1 // comparo con 1
	JNZ fin // si no es 1, fin
sigue: 	SHL [4],1 //shifteo a izq 1 bit
	OR [4],[0] // concateno el bit leido
	JMP otro // repito
fin:	MOV EDX,DS
	ADD EDX,4
	LDL ECX,1
	LHL ECX,4
	MOV EAX,0x1F // write
	SYS 2 
	STO