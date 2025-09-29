1er operando EBX
2do operando ECX
resultado EAX
inicio: MOV EBX,0
       MOV EDX,DS
       LDL ECX,1
       LHL ECX,4
       MOV EAX,1
       SYS 1
       MOV EBX,[EDX] // guardo primer operando en EBX

       MOV EDX,DS
       LDL ECX,1
       LHL ECX,4
       MOV EAX,1
       SYS 1
       MOV ECX,[EDX] // guardo segundo operando en ECX

       COMP ECX,0 
       JZ fin

       XOR EAX, EAX         ; EAX = 0 (resultado)
       XOR EEX, EEX         ; EEX = 0 (signo)
       COMP EBX,0
       JNN check_ecx
        NOT EEX              ; si EBX < 0, toggle signo
        NOT EBX              ; EBX = -EBX
        ADD EBX,1

check_ecx:
        CMP ECX,0
        JNN div_loop
        NOT EEX              ; si ECX < 0, toggle signo
        NOT ECX              ; ECX = -ECX
        ADD ECX,1

div_loop:  
        SUB EBX,ECX 
        JN apply_sign
        ADD EAX,1
apply_sign:
        COMP EFX,0
        JZ fin
        NOT EAX
        ADD EAX,1
        ADD EBX,ECX //corrijo resultado final
        MOV AC,EBX //resto en AC
        JMP fin

zero_div: //muestro mensaje de error
        MOV [3], 'o'
        MOV [2], 'r'
        MOV [1], 'e'
        MOV [0], 'z'
        MOV EDX, DS
        LDL ECX,1
        LHL ECX, 4
        MOV EAX 0x02
        SYS 2
        STOP
fin:    
        MOV [0], [EAX]
        MOV EDX, DS
        LDL ECX, 1
        LHL ECX, 4
        MOV EAX, 1
        SYS 2  // muestra conciente

        MOV [0], AC
        MOV EDX, DS
        LDL ECX, 1
        LHL ECX, 4
        MOV EAX, 1
        SYS 2  // muestra resto
        STOP
