;Suponiendo que no existe la instrucción MUL, crear un algoritmo que reciba en EBX y ECX los
;dos valores y retorne en EAX su producto.
; Algoritmo: EAX = EBX * ECX
; Entradas: EBX, ECX
; Salida:   EAX
inicio:        
        MOV EDX,DS
        MOV EAX,1
        LDL ECX,1
        LDH ECX,4
        SYS 1
        MOV EBX,[EDX]; guardo el primer operando en EBX
        MOV EDX,DS
        ADD EDX,4
        MOV EAX,1
        LDL ECX,1
        LDH ECX,4
        SYS 1
        MOV ECX,[EDX]; guardo el segundo operando en ECX        
        ; ---- Inicialización ----
        XOR EAX, EAX         ; EAX = 0 (resultado)
        XOR AC, AC           ; AC lo usamos como "signo"

        ; ---- Determinar signo del resultado ----        
        CMP EBX, 0
        JNN check_ecx
        NOT AC               ; si EBX < 0, toggle signo
        NOT EBX              ; EBX = -EBX
        ADD EBX, 1
check_ecx:        
        CMP ECX, 0
        JNN mult_loop
        NOT AC               ; si ECX < 0, toggle signo
        NOT ECX              ; ECX = -ECX
        ADD ECX, 1

        ; ---- Bucle de sumas repetidas ----
mult_loop:
        CMP ECX, 0
        JZ apply_sign
        ADD eax, ebx
        SUB ecx, 1
        JMP mult_loop
        ; ---- Aplicar signo final ----
apply_sign:
        CMP ac, 0
        JZ fin
        NOT eax              ; resultado = -EAX
        ADD eax, 1

fin:
        STOP
