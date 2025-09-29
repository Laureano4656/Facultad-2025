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
        ; ---- Inicialización ----
        xor     eax, eax         ; EAX = 0 (resultado)
        xor     ac, ac           ; AC lo usamos como "signo"

        ; ---- Determinar signo del resultado ----
        mov     edx, ebx
        cmp     edx, 0
        jnn     check_ecx
        not     ac               ; si EBX < 0, toggle signo
        not     ebx              ; EBX = -EBX
        add     ebx, 1

check_ecx:
        cmp     ecx, 0
        jnn     mult_loop
        not     ac               ; si ECX < 0, toggle signo
        not     ecx              ; ECX = -ECX
        add     ecx, 1

        ; ---- Bucle de sumas repetidas ----
mult_loop:
        cmp     ecx, 0
        jz      apply_sign
        add     eax, ebx
        sub     ecx, 1
        jmp     mult_loop

        ; ---- Aplicar signo final ----
apply_sign:
        cmp     ac, 0
        jz      fin
        not     eax              ; resultado = -EAX
        add     eax, 1

fin:
        stop