import math

"""
Para cada uno de los siguientes mensajes, emitidos por fuentes de información:

Determinar el alfabeto y las probabilidades de sus símbolos
Obtener la matriz de transición de la fuente
Estimar si se trata de una fuente de memoria nula o no nula
Calcular la entropía de la fuente
Si es una fuente de memoria nula, generar la extensión de orden 2 y calcular su entropía a partir de sus probabilidades
Si es una fuente con memoria, obtener el vector estacionario
"""
def mostrarMatriz(matriz : list[list[float]], titulo : str): 
    print(titulo)
    for fila in matriz:
        print(fila)

def getVecEstacionarioMat(matriz: list[list[float]]) -> list[float]: 
       # Inicializar vector estacionario suponiendo equiprobabilidad
    vec_est = [];
    for i in range(len(matriz)): # Len devuelve el numero de filas
        vec_est.append(1/len(matriz));
    vec_est_nuevo = [0] * len(matriz); # Inicializo todo el vector auxiliar en 0

    # Iterar hasta convergencia
    iteraciones = 100;
    for k in range(iteraciones):
        for i in range(len(matriz)):
            vec_est_nuevo[i] = 0;
            for j in range(len(matriz)):
                vec_est_nuevo[i] += vec_est[j] * matriz[i][j];
        vec_est = vec_est_nuevo[:]; # Hago una copia para no tener referencias
    return vec_est;

def calcularEntropiaFuenteMarkov(mat: list[list[float]], vec_est: list[float]) -> float:
    entropia = 0;
    for j in range(len(mat)):
        sum = 0;
        for i in range(len(mat)):
            if mat[i][j] != 0:
                sum += mat[i][j] * math.log2(1/mat[i][j]); # Esta en base 2
        entropia += vec_est[j] * sum;
    return entropia;

def calcExtensionN(fuente: list[str], probabilidades: list[float], n: int) -> tuple[list[str], list[float]]: 
    if n == 1:
        return fuente,probabilidades
    else:
        nueva_fuente = []
        nuevas_probabilidades = []
        anterior_fuente,anteriores_probabilidades = calcExtensionN(fuente,probabilidades,n-1)
        for i in range(len(anterior_fuente)):
            for j in range(len(fuente)):
                nueva_combinacion = anterior_fuente[i]+fuente[j]
                nueva_probabilidad = anteriores_probabilidades[i]*probabilidades[j]
                nueva_fuente.append(nueva_combinacion)
                nuevas_probabilidades.append(nueva_probabilidad)
        return nueva_fuente,nuevas_probabilidades

def getInformacion(probabilidades: list[float]) -> list[float]: 
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

def getMatriz(alphabet: list[str],msg: str) -> list[list[float]]:
    n = len(alphabet);
    mat = [];

    # Inicializo la matriz en 0
    for i in range(n):
        mat.append([0] * n);

    for j in alphabet:
        for i in alphabet:
            aux = j + i;
            for k in range(len(msg) - 1):
                if msg[k] + msg[k + 1] == aux:
                    mat[alphabet.index(i)][alphabet.index(j)] += 1;
    
    for j in range(n):
        sum = 0;
        for i in range(n):
            sum += mat[i][j];
        if sum != 0:
            for i in range(n):
                mat[i][j] = mat[i][j] / sum;
    return mat;

def isMemoriaNula(matriz: list[list[float]],tolerancia: float) -> bool: 
    maxima_dif = []
    for i in range(len(matriz)):
        maxima_dif.append(max(matriz[i])-min(matriz[i]))
    maxima = max(maxima_dif)
    if maxima<tolerancia:
        return True
    else:
        return False


def multiplicar_matrices(A, B):
    """
    Multiplica dos matrices A y B sin usar numpy.
    """
    filas_A = len(A)
    cols_A = len(A[0])
    filas_B = len(B)
    cols_B = len(B[0])

    if cols_A != filas_B:
        raise ValueError("Las dimensiones no coinciden para multiplicar.")

    # Crear matriz resultado llena de ceros
    C = [[0.0 for _ in range(cols_B)] for _ in range(filas_A)]

    for i in range(filas_A):
        for j in range(cols_B):
            for k in range(cols_A):
                C[i][j] += A[i][k] * B[k][j]
    return C

def tiene_ceros(matriz, tolerancia=1e-9):
    """
    Verifica si la matriz tiene algún elemento que sea (prácticamente) cero.
    Usamos tolerancia para evitar errores de punto flotante.
    """
    for fila in matriz:
        for valor in fila:
            if valor <= tolerancia:
                return True
    return False

def verificar_regularidad(matriz, max_potencia=None):
    """
    Verifica si una matriz es regular elevándola a potencias sucesivas
    hasta encontrar una matriz sin ceros.
    """
    n = len(matriz)
    
    # Límite teórico: Si es regular, debería ocurrir antes de n^2 pasos
    # (Cota de Wielandt: n^2 - 2n + 2). Ponemos un límite de seguridad.
    if max_potencia is None:
        max_potencia = n * n + 2

    matriz_actual = matriz # Empezamos con M^1
    
    print(f"Probando regularidad para matriz {n}x{n}...")

    for k in range(1, max_potencia + 1):
        if not tiene_ceros(matriz_actual):
            print(f"¡Éxito! La matriz es REGULAR en la potencia k={k}.")
            # Opcional: Mostrar la matriz resultante
            # for fila in matriz_actual: print([round(x, 4) for x in fila])
            return True
        
        # Multiplicamos por la matriz original para obtener la siguiente potencia
        # M^(k+1) = M^k * M
        matriz_actual = multiplicar_matrices(matriz_actual, matriz)

    print(f"No se encontró regularidad hasta la potencia k={max_potencia}.")
    return False

msg1 = "+-/+/-//-/*-/**-*---////-+--*+*/-----/--+/++--*/-+"

alfabeto1,probs1 = getAlfabetoyProbabilidades(msg1)

matrizTransicion1 = getMatriz(alfabeto1,msg1)

esMemoriaNula1 = isMemoriaNula(matrizTransicion1,1e-10)

print("Mensaje 1")
print("Alfabeto:", alfabeto1)
print("Probabilidades:", probs1)
mostrarMatriz(matrizTransicion1,"Matriz de Transición" )
print("¿Es memoria nula?:", esMemoriaNula1)
entropia1 = getEntropia(probs1)
print("Entropía:", entropia1)

extension2_1,probsExtension2_1 = calcExtensionN(alfabeto1,probs1,2)
entropiaExtension2_1 = getEntropia(probsExtension2_1)
for simbolo, prob in zip(extension2_1, probsExtension2_1):
    print(f"Símbolo: {simbolo}, Probabilidad: {prob}")
print("Entropía de la extensión de orden 2:", entropiaExtension2_1)

msg2 = "-+-+*//++///*/-////+---////-+/+--+-+/-/+-+/-+*++//"

alfabeto2,probs2 = getAlfabetoyProbabilidades(msg2)

matrizTranscion2 = getMatriz(alfabeto2,msg2)
esMemoriaNula2 = isMemoriaNula(matrizTranscion2,1e-10)

print("\nMensaje 2")
print("Alfabeto:", alfabeto2)
print("Probabilidades:", probs2)
print("Verificando regularidad de la matriz de transición...")

mostrarMatriz(matrizTranscion2,"Matriz de Transición" )
print("¿Es memoria nula?:", esMemoriaNula2)
vectorEstacionario2 = getVecEstacionarioMat(matrizTranscion2)
print("Vector estacionario:", vectorEstacionario2)
entropia2 = calcularEntropiaFuenteMarkov(matrizTranscion2,vectorEstacionario2)
print("Entropía:", entropia2)