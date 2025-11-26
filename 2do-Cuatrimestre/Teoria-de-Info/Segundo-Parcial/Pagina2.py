import math

"""
Dadas las siguientes secuencias de entrada y salida de un canal:

Obtener las probabilidades a priori y la matriz del canal
Informar si se trata de un canal sin ruido y/o determinante
Calcular la equivocación, la pérdida y la información mutua
Efectuar todas las reducciones suficientes posibles en el canal
Determinar la capacidad y la probabilidad de error del canal
Detectar y/o corregir los errores en la secuencia de entrada
Aclaración: asumir que la secuencia de entrada contiene un mensaje representado con código ASCII y sus bits de paridad vertical, longitudinal y cruzada.

Entrada:	10101001
            10101110
            10101010
            10100101
Salida:	UUVTWUUUUUVUUWTUWTUTTTWUUUTUUVTV
"""
def mostrarMatriz(matriz : list[list[float]], titulo : str): 
    print(titulo)
    for fila in matriz:
        print(fila)

def byteArrayToStringWithParity(byte_array: bytearray) -> str:
    original_message = ""
    
    errors = 0
    
    #convierto el byte array a una matriz de floats
    matriz = []
    for byte in byte_array:
        codigo_ascii_con_paridad = format(byte, '08b')  # Obtengo el codigo ASCII en binario de 8 bits
        fila = [int(bit) for bit in codigo_ascii_con_paridad]; # Convierto el string a una lista de enteros
        matriz.append(fila)
    
    #mostrarMatriz(matriz, "Matriz con paridad")

    # creo una estructura para saber las posiciones de error
    posiciones_error = []

    # Verificar la paridad cruzada
    sumPrimeraFila = sum(matriz[0])
    primeraColumna = [ matriz[i][0] for i in range(len(matriz)) ]
    sumPrimeraColumna = sum(primeraColumna)
    
    if (sumPrimeraColumna % 2) != (sumPrimeraFila % 2):
        print("Error en paridad cruzada")
        return ""  # No se puede corregir el error

    # Verificar la paridad longitudinal
    for j in range(8):
        count = 0
        for i in range(1, len(matriz)):  # Empiezo desde 1 para saltar la fila de paridad VRC            
            if matriz[i][j] == 1:
                count += 1
        parity_bit = count % 2
        if parity_bit != matriz[0][j]:
            print(f"Error en paridad longitudinal en columna {j}")
            errors += 1
            posiciones_error.append((j, j))  # 'L' para longitudinal
    print(f"Errores detectados hasta ahora: {errors}")
    # Verificar la paridad VRC
    for i in range(1, len(matriz)):  # Empiezo desde 1 para saltar la fila de paridad VRC
        fila = matriz[i][:-1]  # Saco la última columna que es la de paridad
        cantidad_1s = sum(fila)
        parity_bit = cantidad_1s % 2        
        # if parity_bit != matriz[i][-1]:  # Si la paridad no es correcta
        #     if posiciones_error.count((i, i)) <= 0:  # Si no se detectó un error longitudinal en esta fila
        #         errors += 1
        #         print(f"Error en paridad VRC en fila {i}")
        #         if errors > 1:
        #             return ""  # No se puede corregir el error
        #         posiciones_error.append((i, i))  # 'V' para VRC
        # else:
            # Si la paridad es correcta, decodifico el caracter
        codigo_ascii = ''.join([str(bit) for bit in fila])  # Convierto la lista de enteros a un string
        caracter = chr(int(codigo_ascii, 2))  # Convierto el codigo ASCII a un caracter
        original_message += caracter
    print(f"Cantidad de errores detectados: {errors}")
    # Corregir errores si es posible
    # if errors == 1:
    #     error_pos = posiciones_error[0]
    #     fila_error = error_pos[0]
    #     columna_error = error_pos[1]
    #     matriz[fila_error][columna_error] ^= 1  # Corregir el bit erróneo
    #     print(f"Corrigiendo error en fila {fila_error}, columna {columna_error}")
    #     # Decodifico el mensaje corregido
    #     original_message = ""
    #     for i in range(1, len(matriz)):  # Empiezo desde 1 para saltar la fila de paridad VRC
    #         fila = matriz[i][:-1]  # Saco la última columna que es la de paridad
    #         codigo_ascii = ''.join([str(bit) for bit in fila])  # Convierto la lista de enteros a un string            
    #         caracter = chr(int(codigo_ascii, 2))  # Convierto el codigo ASCII a un caracter
    #         original_message += caracter

    return original_message
def getProbabilidadesAPosteriori(probsPriori: list[float], matrizCanal: list[list[float]], probs_salida: list[float]) -> list[list[float]]:
    num_simbolos_entrada = len(probsPriori)
    num_simbolos_salida = len(matrizCanal[0])
    probs_posteriori = [[0.0] * num_simbolos_entrada for _ in range(num_simbolos_salida)]

    for j in range(num_simbolos_salida):
        for i in range(num_simbolos_entrada):
            if probs_salida[j] > 0:
                probs_posteriori[j][i] = ( matrizCanal[i][j] *probsPriori[i] ) / probs_salida[j]
            else:
                probs_posteriori[j][i] = 0.0

    return probs_posteriori
def getAlfabetoyProbabilidades(cadena) -> tuple[list[str], list[float]]: 
    alfabeto = list()
    apariciones = list()
    for simbolo in cadena:
        if (simbolo in alfabeto):
            apariciones[alfabeto.index(simbolo)]+=1
        else:
            apariciones.append(1)
            alfabeto.append(simbolo)
    probabilidades = [aparicion/len(cadena) for aparicion in apariciones]
    # Ordeno el alfabeto y las probabilidades en base al alfabeto
    alfabeto_prob = sorted(zip(alfabeto, probabilidades))
    alfabeto, probabilidades = zip(*alfabeto_prob)
    return alfabeto,probabilidades
def getMatrizCanal(entrada:str, salida:str) ->list:

    if len(entrada) != len(salida):
        print("Error: Las secuencias de entrada y salida deben tener la misma longitud.")
        return None

    # 1. Identificar símbolos únicos y ordenarlos para consistencia
    simbolos_entrada = getAlfabetoyProbabilidades(entrada)[0]
    simbolos_salida = getAlfabetoyProbabilidades(salida)[0]
    
    # Mapeo de símbolo a índice para fácil acceso
    # El mapa tiene como clave el símbolo y como valor su índice en la matriz
    mapa_entrada = {simbolo: i for i, simbolo in enumerate(simbolos_entrada)}
    mapa_salida = {simbolo: i for i, simbolo in enumerate(simbolos_salida)}

    # 2. Contar ocurrencias para el numerador y denominador
    # Diccionario para contar las apariciones totales de cada símbolo de entrada (denominador)
    # este diccionario tiene como clave el símbolo y como valor la cantidad de apariciones
    conteo_entrada = {simbolo: 0 for simbolo in simbolos_entrada}
    
    # Matriz para contar los pares (entrada, salida) (numerador)
    num_filas = len(simbolos_entrada)
    numColumnas = len(simbolos_salida)
    conteo_pares = [[0] * numColumnas for _ in range(num_filas)]

    # Recorrer las secuencias para llenar los contadores
    for i in range(len(entrada)):
        sim_in = entrada[i]
        sim_out = salida[i]

        # Incrementar el conteo total del símbolo de entrada
        conteo_entrada[sim_in] += 1
        
        # Incrementar el conteo del par (entrada, salida)
        idx_fila = mapa_entrada[sim_in]
        idxColumna = mapa_salida[sim_out]
        conteo_pares[idx_fila][idxColumna] += 1

    # 3. Calcular probabilidades y construir la matriz final
    matrizCanal = [[0.0] * numColumnas for _ in range(num_filas)]

    for simbolo_in, i in mapa_entrada.items():
        total_apariciones = conteo_entrada[simbolo_in] # cantidad de apariciones del símbolo de entrada
        # Evitar división por cero
        if total_apariciones > 0:
            # Calcular P(bj/ai) para cada símbolo de salida
            for j in range(numColumnas):
                matrizCanal[i][j] = conteo_pares[i][j] / total_apariciones
    
    return matrizCanal
def isSinRuido(matriz: list[list[float]]) -> bool:
    """
    Verifica si un canal es sin ruido.
    Un canal es sin ruido si cada columna de la matriz tiene exactamente un valor 1 y el resto son 0.
    """
    for col in range(len(matriz[0])):
        sumCol = 0
        for row in range(len(matriz)):
            if matriz[row][col] != 0:
                sumCol += 1
        if sumCol != 1:
            return False
    return True

def isDeterminante(matriz: list[list[float]]) -> bool:
    """
    Verifica si un canal es determinante.
    Un canal es determinante si cada fila de la matriz tiene exactamente un valor 1 y el resto son 0,
    y además, cada columna tiene exactamente un valor 1 y el resto son 0.
    """
    # verificar filas
    for row in range(len(matriz)):
        if matriz[row].count(1) != 1 or matriz[row].count(0) != len(matriz[row]) - 1:
            return False
        
    return True

def getEquivocacionRuido(probsPriori: list[float], matrizCanal: list[list[float]]) -> float:
    """
    Calcula la equivocación (ruido) H(A/B) por definición.
    
    Definición:
    H(A/B) = sum_b P(b) * H(A/b)
    donde H(A/b) = + sum_a P(a/b) * log2(1/P(a/b))
    
    Returns:
        float: El valor de la equivocación H(A/B) en bits.
    """
       
    # --- 2. Calcular Probabilidad de Salida P(B) ---
    p_b = getProbabilidadesSalida(probsPriori, matrizCanal)
    
    # --- 3. Calcular Probabilidad "Backward" P(A/B) ---
    probsPosteriori = getProbabilidadesAPosteriori(probsPriori, matrizCanal, p_b)
    
    # --- 4. Calcular P(a,b) ---
    matrizSimultaneas = getMatrizSucesosSimultaneos(probsPriori, matrizCanal)
    ruido = 0.0
    for i in range(len(matrizSimultaneas)):        
        for j in range(len(matrizSimultaneas[0])):
            ruido += matrizSimultaneas[i][j] * math.log2(1/probsPosteriori[j][i]) if probsPosteriori[j][i] > 0 else 0.0
    return ruido

def getPerdida(probsPriori: list[float], matrizCanal: list[list[float]]) -> float:
    numX = len(probsPriori)
    numY = len(matrizCanal[0])
    perdida = 0.0

    for i in range(numX):
        if probsPriori[i] <= 0:
            continue
        h_entropia_condicional = 0.0
        for j in range(numY):
            if matrizCanal[i][j] > 0:
                h_entropia_condicional += matrizCanal[i][j] * math.log2(1/matrizCanal[i][j])
                
        perdida += probsPriori[i] * h_entropia_condicional

    return perdida

def getMatrizSucesosSimultaneos(probsPriori: list[float], matrizCanal: list[list[float]]) -> list[list[float]]:
    num_simbolos_salida = len(matrizCanal[0])
    probs_simultaneas = [[0.0] * num_simbolos_salida for _ in range(len(probsPriori))]

    for i in range(len(probsPriori)):
        for j in range(num_simbolos_salida):
            probs_simultaneas[i][j] = probsPriori[i] * matrizCanal[i][j]

    return probs_simultaneas

def getProbabilidadesSalida(probsPriori: list[float], matrizCanal: list[list[float]]) -> list[float]:
    
    num_simbolos_salida = len(matrizCanal[0])
    probs_salida = [0.0] * num_simbolos_salida

    for j in range(num_simbolos_salida):
        for i in range(len(probsPriori)):
            probs_salida[j] += probsPriori[i] * matrizCanal[i][j]

    return probs_salida

def getInformacionMutua(probsPriori: list[float], matrizCanal: list[list[float]]) -> float:       
    probsSimultaneas = getMatrizSucesosSimultaneos(probsPriori, matrizCanal)
    probsSalida = getProbabilidadesSalida(probsPriori, matrizCanal)
    informacionMutua1 = 0.0
    for i in range(len(probsPriori)):
        for j in range(len(probsSalida)):
            p_xy = probsSimultaneas[i][j]
            p_x = probsPriori[i]
            p_y = probsSalida[j]
            if p_xy > 0:
                informacionMutua1 += p_xy * math.log2(p_xy / (p_x * p_y))

    return informacionMutua1
def verificarColumnasReducibles(matriz: list[list[float]], col1: int, col2: int) -> bool:
    """
    Verifica si dos columnas de la matriz se pueden combinar en una reducción suficiente.
    Dos columnas se pueden combinar si para cada fila los elementos son iguales o multiplicables.
    Debo considerar numeros flotantes.
    Ejemplo:
    0.4 y 0.6 son multiplicables (0.6 es 1.5 * 0.4)
    """
    
    constantList = []
    for i in range(len(matriz)):
        val1 = matriz[i][col1]
        val2 = matriz[i][col2]
        if val1 == 0 and val2 == 0:
            if len(constantList) != 0:
                constantList.append(constantList[-1])  # agrego el ultimo valor para mantener la consistencia
        elif val1 == 0 or val2 == 0:    
            return False
        else:
            constantList.append(val2 / val1)
    
    firstConstant = None
    for constant in constantList:
        if constant != 0:
            firstConstant = constant
            break

    if firstConstant is None:        
        return True

    for constant in constantList:
        if constant != firstConstant:            
            return False

    return True

def generarMatrizDeterminante(matriz: list[list[float]], col1: int, col2: int) -> list[list[float]]:
    """
    Genera la matriz del canal determinante para combinar 'col1' y 'col2'.
    La nueva columna combinada estará en el índice 'col1'.
    
    (Asegura que col1 sea siempre la más pequeña para que sea el nuevo índice)
    """
    if col1 > col2:
        col1, col2 = col2, col1 # col1 siempre será el índice menor
        
    cantFilasOrig = len(matriz[0]) # Filas del determinante = Columnas de la matriz original
    cantColumnasDest = len(matriz[0]) - 1 # Columnas del determinante = Columnas de la matriz nueva
    
    nuevaMatriz = [[0 for _ in range(cantColumnasDest)] for _ in range(cantFilasOrig)]
    
    # 1. Mapear las dos columnas a combinar
    # La col1 original -> a la nueva col1
    nuevaMatriz[col1][col1] = 1
    # La col2 original -> también a la nueva col1
    nuevaMatriz[col2][col1] = 1
    
    # 2. Mapear el resto de columnas (identidad)
    colDestino = 0
    for colOrig in range(cantFilasOrig):
        
        # Ignoramos las columnas que ya mapeamos
        if colOrig == col1 or colOrig == col2:
            continue
            
        # Si la columna de destino es 'col1', la saltamos
        # porque ya está ocupada por la combinación
        if colDestino == col1:
            colDestino += 1
            
        nuevaMatriz[colOrig][colDestino] = 1
        colDestino += 1
        
    # utils.mostrarMatriz(nuevaMatriz, f"Matriz determinante para {col1} y {col2}")
    return nuevaMatriz
def getCanalCompuesto(canalA: list[list[float]], canalB: list[list[float]]) -> list[list[float]]:
    """
    Obtiene la matriz del canal compuesto en serie de dos canales.
    El canal compuesto se obtiene multiplicando las matrices de los dos canales.
    """
    filasA = len(canalA)
    columnasA = len(canalA[0])
    filasB = len(canalB)
    columnasB = len(canalB[0])
    
    if columnasA != filasB:
        raise ValueError("El número de columnas del primer canal debe ser igual al número de filas del segundo canal.")
    
    canalCompuesto = [[0 for _ in range(columnasB)] for _ in range(filasA)]
    
    for i in range(filasA):
        for j in range(columnasB):
            for k in range(columnasA):
                canalCompuesto[i][j] += canalA[i][k] * canalB[k][j]        
    return canalCompuesto
def isUniforme(matriz: list[list[float]]) -> bool:
    """
    Un canal es uniforme si cada fila consiste en una permutación
    arbitraria de los términos de la primera fila.
    """
    primeraFila = matriz[0]
    for fila in matriz[1:]:
        if sorted(fila) != sorted(primeraFila):
            return False
    return True
def isSimetrico(matriz: list[list[float]]) -> bool:
    """
    En un canal simétrico los elementos de las filas y las columnas
    son iguales pero permutados.
    """
    primeraFila = matriz[0]
    for fila in matriz[1:]:
        if sorted(fila) != sorted(primeraFila):
            return False
    # ahora verifico las columnas
    primeraColumna = [matriz[i][0] for i in range(len(matriz))]
    for j in range(1, len(matriz[0])):
        columna = [matriz[i][j] for i in range(len(matriz))]
        if sorted(columna) != sorted(primeraColumna):
            return False
    return True

def getInformacion(probabilidades): 
    info = list()
    for prob in probabilidades:
        if prob>0:
            info.append(math.log2(1/prob))
        else:
            info.append(0)
    return info
def getEntropia(probabilidades): 
    info = getInformacion(probabilidades)
    H = 0
    for I,P in zip(info,probabilidades):
        H += I*P
    return H

def isCanalBSC(matriz: list[list[float]]) -> bool:
    """
    Verifica si un canal es un canal BSC (Binary Symmetric Channel).
    Un canal BSC tiene dos entradas y dos salidas, y la probabilidad de error es la misma para ambas entradas.
    """
    if len(matriz) != 2 or len(matriz[0]) != 2:
        return False
    pError = matriz[0][1]
    if matriz[1][0] != pError:
        return False
    return True
def calcCapacidad(matriz: list[list[float]]) -> float:
    """
    Calcula la capacidad del canal dado su matriz de transición.
    La capacidad se define como el máximo de la información mutua sobre todas las distribuciones de probabilidad de entrada posibles.
    """
    numEntradas = len(matriz)
    numSalidas = len(matriz[0])

    if (isDeterminante(matriz)):
        print("Canal determinante")
        return math.log2(numSalidas)
    
    if (isSinRuido(matriz)):
        print("Canal sin ruido")
        return math.log2(numEntradas)
    
    if (isSimetrico(matriz)):
        print("Canal simétrico")
        # para canales simétricos tengo que obtener la entropía del canal
        primeraFila = matriz[0]
        return math.log2(numEntradas) - getEntropia(primeraFila)
    
    if (isUniforme(matriz)):
        print("Canal uniforme")
        # debo calcular la entropia de la primera fila
        primeraFila = matriz[0]
        return math.log2(numEntradas) - getEntropia(primeraFila)        

    if (isCanalBSC(matriz)):
        print("Canal BSC")
        pError = matriz[0][1]
        return 1 - (-pError * math.log2(pError) - (1 - pError) * math.log2(1 - pError))

def maxReduccion(matriz: list[list[float]]) -> list[list[float]]:
    
    matrizReducida = [fila[:] for fila in matriz]
    seHizoUnaReduccion = True    
    while seHizoUnaReduccion:
        seHizoUnaReduccion = False
        columnasReducida = len(matrizReducida[0])

        if columnasReducida < 2:
            break

        # Bucle 'break' anidado
        # Usamos esto para poder salir de ambos bucles 'for'
        # cuando se encuentra una reducción
        
        # Necesitamos bucles anidados para comprobar CADA par de columnas (col1, col2)
        for col1 in range(columnasReducida):
            # Empezamos col2 desde col1 + 1 para no comparar (0,0) ni duplicar (1,0)
            for col2 in range(col1 + 1, columnasReducida):
                
                if verificarColumnasReducibles(matrizReducida, col1, col2):
                    # Hay un par reducible
                    matrizDeterminante = generarMatrizDeterminante(matrizReducida, col1, col2)
                    matrizReducida = getCanalCompuesto(matrizReducida, matrizDeterminante)                    
                    seHizoUnaReduccion = True                    
                    # Rompemos AMBOS bucles 'for' para reiniciar el 'while True'
                    # con la nueva matriz reducida.
                    break # Rompe el bucle 'col2'
            
            if seHizoUnaReduccion:
                break # Rompe el bucle 'col1'        
            
    return matrizReducida

def convertMatrixToByteArray(matriz: list[list[float]]) -> bytearray:
    byte_array = bytearray()
    for fila in matriz:
        codigo_ascii = ''.join([str(bit) for bit in fila])  # Convierto la lista de enteros a un string
        byte_array.append(int(codigo_ascii, 2))  # Convierto el codigo ASCII a un caracter
    return byte_array

def calcProbabilidadError(probsPriori: list[float], matriz: list[list[float]]) -> float:
    """
    Calcula la probabilidad de error utilizando la regla de decisión de máxima posibilidad.
    """
    # debo encontrar los maximos de la matriz por columna
    numEntradas = len(matriz)
    numSalidas = len(matriz[0])
    indicesMaximos = [-1 for _ in range(numSalidas)]
    for j in range(numSalidas):
        maxVal = -1
        indiceMax = -1
        for i in range(numEntradas):
            if matriz[i][j] > maxVal:
                maxVal = matriz[i][j]
                indiceMax = i
        indicesMaximos[j] = indiceMax

    # Calculo la probabilidad de error sumando las probabilidades excepto las de los maximos
    probabilidadError = 0.0
    for j in range(numSalidas):
        for i in range(numEntradas):
            if i != indicesMaximos[j]:
                probabilidadError += probsPriori[i] * matriz[i][j]

    return probabilidadError

entrada = "10101001101011101010101010100101"
salida = "UUVTWUUUUUVUUWTUWTUTTTWUUUTUUVTV"
matrizEntrada = [
    [1,0,1,0,1,0,0,1],
    [1,0,1,0,1,1,1,0],
    [1,0,1,0,1,0,1,0],
    [1,0,1,0,0,1,0,1]
]

probabilidadesEntrada = getAlfabetoyProbabilidades(entrada)[1]
entropiaEntrada = getEntropia(probabilidadesEntrada)
matrizCanal = getMatrizCanal(entrada,salida)

esSinRudo = isSinRuido(matrizCanal)
esDeterminante = isDeterminante(matrizCanal)

equivocacion = getEquivocacionRuido(probabilidadesEntrada,matrizCanal)
perdida = getPerdida(probabilidadesEntrada,matrizCanal)
infoMutua = getInformacionMutua(probabilidadesEntrada,matrizCanal)


probsSalida =getProbabilidadesSalida(probabilidadesEntrada, matrizCanal)
matrizReducida = maxReduccion(matrizCanal)
capacidadCanal = calcCapacidad(matrizCanal)
probErrorCanal = calcProbabilidadError(probabilidadesEntrada,matrizReducida)

byteArray = convertMatrixToByteArray(matrizEntrada)
print("Byte array de la entrada: ",byteArray)
salidaObtenida = byteArrayToStringWithParity(byteArray)
print("Entropia entrada: ",entropiaEntrada)
print("Probabilidades a priori: ",probabilidadesEntrada)

mostrarMatriz(matrizCanal,"Matiz del canal:")
print("Canal sin ruido: ",esSinRudo)
print("Canal determinante: ",esDeterminante)
print("Equivocacion del canal: ",equivocacion)
print("Perdida del canal: ",perdida)
print("Informacion mutua del canal: ",infoMutua)
print("Matriz reducida del canal: ")
mostrarMatriz(matrizReducida, "Matriz reducida del canal:")
print("Capacidad del canal: ",capacidadCanal)
print("Probabilidad de error del canal: ",probErrorCanal)
print("Salida obtenida: ", salidaObtenida)