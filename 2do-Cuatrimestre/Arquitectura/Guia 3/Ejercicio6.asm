; 6. Suponiendo que no existe la instrucción DIV, crear un algoritmo que reciba en EBX y ECX los
; dos valores y retorne en EAX el resultado de la división, dejando en AC el resto.
inicio:
        MOV EBX,0
        MOV EDX,DS
        XOR EAX,EAX
        LDL ECX,1
        LDH ECX,4
        SYS 1
        MOV EBX,[EDX]; guardo el primer operando en EBX
        MOV EDX,DS
        MOV EDX,DS
        MOV EAX,1
        LDL ECX,1
        LDH ECX,4
        SYS 1
        MOV ECX,[EDX]; guardo el segundo operando en ECX
        COMP EDX,0
        JZ fin
        MOV EDX,DS
        MOV EDX,DS
        MOV EAX,1
        XOR EEX,EEX ; EEX = 0 (signo)
        CMP EBX,0
        JNN check_ecx
        NOT EEX ; si EBX < 0, toggle signo
        NOT EBX
        ADD EBX,1
check_ecx:
        CMP ECX,0
        JNN div_loop
        NOT EEX ; si ECX < 0, toggle signo
        NOT ECX
        ADD ECX,1
div_loop:
        SUB EBX,ECX
        JN apply_sign
        ADD EAX,1
apply_sign:
        CMP EFX,0
        JZ fin
        NOT EAX
        ADD EAX,1
        ADD EBX,ECX ;Corrijo para que no quede negativo y conseguir el resto
        MOV AC,EBX ; pongo el resto en AC
        JMP fin
zero_div:
        MOV [3], 'o'
        MOV [2], 'r'
        MOV [1], 'e'
        MOV [0], 'Z'
        MOV EDX, DS
        ADD EDX, 3
        LDH ECX, 1
        LDL ECX, 4
        MOV EAX, 0x02
        SYS 0x2
        STOP
fin:
        MOV EDX,DS
        MOV [EAX],EAX
        LDH ECX,1
        LDL ECX,4
        MOV EAX,1
        SYS 2
        MOV EDX,DS
        MOV [EDX],AD
        LDH ECX,1
        LDL ECX,4
        MOV EAX,1
        SYS 2
        STOP