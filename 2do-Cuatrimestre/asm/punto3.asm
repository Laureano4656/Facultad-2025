    MOV edx,DS // buffer
    LDL ECX,1
    LHL ECX,4 
    MOV EAX,1
    SYS 1
    
    MOV edx,DS 
    LDL ECX,1
    LHL ECX,4 
    MOV EAX,0x10
    SYS 2