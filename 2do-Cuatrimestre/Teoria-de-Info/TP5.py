import math
import FuncTeoriaDeLaInfo as ut
'''2. Codificar una función en Python que reciba como parámetros dos cadenas de caracteres
que contengan secuencias de entrada y de salida de un canal y retorne la matriz que
representa dicho canal.
'''
print("Ejercicio 2")

## recibe entrada y salida como cadenas de caracteres y retorna la matriz del canal
def getMatrizCanal(entrada:str, salida:str) ->list:

    if len(entrada) != len(salida):
        print("Error: Las secuencias de entrada y salida deben tener la misma longitud.")
        return None

    # 1. Identificar símbolos únicos y ordenarlos para consistencia
    simbolos_entrada = ut.getAlfabetoyProbabilidades(entrada)[0]
    simbolos_salida = ut.getAlfabetoyProbabilidades(salida)[0]
    
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
        total_apariciones = conteo_entrada[simbolo_in]
        if total_apariciones > 0:
            for j in range(numColumnas):
                matrizCanal[i][j] = conteo_pares[i][j] / total_apariciones
    
    return matrizCanal



# Ejemplo de uso
entrada = "abcacaabbcacaabcacaaabcaca"
salida = "01010110011001000100010011"
matrizCanal = getMatrizCanal(entrada, salida)
for fila in matrizCanal:
    print(fila)

print("--------------------------------------------------------")
print("Ejercicio 3")
'''
Dadas las siguientes secuencias de entrada y sus respectivas salidas, las cuales describen
el comportamiento de los canales, calcular las probabilidades a priori y la matriz del canal.

'''
entrada1 = "1101011001101010010101010100011111"
salida1 = "1001111111100011101101010111110110"
matrizCanal1 = getMatrizCanal(entrada1, salida1)
probabilidades_entrada1 = ut.getAlfabetoyProbabilidades(entrada1)[1]

print("Canal 1:")
print("Probabilidades a priori de la entrada:")
for simbolo, prob in zip(ut.getAlfabetoyProbabilidades(entrada1)[0], probabilidades_entrada1):
    print(f"Símbolo: {simbolo}, Probabilidad: {prob:.4f}")

print("Matriz del canal:")
for fila in matrizCanal1:
    print(fila)
    
entrada2 = "110101100110101100110101100111110011"
salida2 = "110021102110022010220121122100112011"
matrizCanal2 = getMatrizCanal(entrada2, salida2)
probabilidades_entrada2 = ut.getAlfabetoyProbabilidades(entrada2)[1]
print("\nCanal 2:")
print("Probabilidades a priori de la entrada:")
for simbolo, prob in zip(ut.getAlfabetoyProbabilidades(entrada2)[0], probabilidades_entrada2):
    print(f"Símbolo: {simbolo}, Probabilidad: {prob:.4f}")
print("Matriz del canal:")
for fila in matrizCanal2:
    print(fila)

print("--------------------------------------------------------")
print("Ejercicio 4")
'''Dado un canal binario con entradas equiprobables y cuyas salidas siempre son iguales a
las entradas, obtener las probabilidades de salida, a posteriori y de los eventos
simultáneos. Analizar los resultados obtenidos.
'''
print("--------------------------------------------------------")

print("Ejercicio 5")
'''
Volver a realizar los cálculos del ejercicio anterior, pero considerando las probabilidades a
priori P(0) = 0.2 y P(1) = 0.8. Comparar los resultados obtenidos.
'''

def getProbabilidadesSalida(probsPriori: list[float], matrizCanal: list[list[float]]) -> list[float]:
    
    num_simbolos_salida = len(matrizCanal[0])
    probs_salida = [0.0] * num_simbolos_salida

    for j in range(num_simbolos_salida):
        for i in range(len(probsPriori)):
            probs_salida[j] += probsPriori[i] * matrizCanal[i][j]

    return probs_salida

def getProbabilidadesSalidaConMsg(entrada: str, salida: str) -> list:
    matrizCanal = getMatrizCanal(entrada, salida)
    probsPriori = ut.getAlfabetoyProbabilidades(entrada)[1]
    num_simbolos_salida = len(matrizCanal[0])
    probs_salida = [0.0] * num_simbolos_salida

    for j in range(num_simbolos_salida):
        for i in range(len(probsPriori)):
            probs_salida[j] += probsPriori[i] * matrizCanal[i][j]

    return probs_salida

def getProbabilidadesSimultaneasConMsg(entrada: str, salida: str) -> list:
    matrizCanal = getMatrizCanal(entrada, salida)
    probsPriori = ut.getAlfabetoyProbabilidades(entrada)[1]
    num_simbolos_salida = len(matrizCanal[0])
    probs_simultaneas = [[0.0] * num_simbolos_salida for _ in range(len(probsPriori))]

    for i in range(len(probsPriori)):
        for j in range(num_simbolos_salida):
            probs_simultaneas[i][j] = probsPriori[i] * matrizCanal[i][j]

    return probs_simultaneas

def getProbabilidadesSimultaneas(probsPriori: list, matrizCanal: list) -> list:
    num_simbolos_salida = len(matrizCanal[0])
    probs_simultaneas = [[0.0] * num_simbolos_salida for _ in range(len(probsPriori))]

    for i in range(len(probsPriori)):
        for j in range(num_simbolos_salida):
            probs_simultaneas[i][j] = probsPriori[i] * matrizCanal[i][j]

    return probs_simultaneas

probsPriori = [0.2, 0.8]
matrizCanal_binario = [[1.0, 0.0], [0.0, 1.0]]  # Canal sin ruido
salidas = getProbabilidadesSalida(probsPriori, matrizCanal_binario)
simultaneas = getProbabilidadesSimultaneas(probsPriori, matrizCanal_binario)
print("Probabilidades de salida con P(0)=0.2 y P(1)=0.8:")
for i, prob in enumerate(salidas):
    print(f"P(salida={i}) = {prob:.4f}")
    
print("Probabilidades simultáneas con P(0)=0.2 y P(1)=0.8:")
for i in range(len(simultaneas)):
    for j in range(len(simultaneas[0])):
        print(f"P(entrada={i}, salida={j}) = {simultaneas[i][j]:.4f}")
        

print("--------------------------------------------------------")
print("Ejercicio 6")
'''
Considerar un canal que recibe mensajes de un alfabeto A = { a, b, c }, con probabilidades
P = { 0.3, 0.3, 0.4 }, y entrega mensajes con un alfabeto B = { 1, 2, 3 }, caracterizado por la
siguiente matriz de probabilidades condicionales:
[0.4,0.4,0.2]
[0.3,0.2,0.5]
[0.3,0.4,0.3]
a. Calcular las probabilidades de los símbolos de salida
b. Obtener las probabilidades a posteriori del canal
c. Determinar las probabilidades de los eventos simultáneos
'''

def getProbabilidadesAPosteriori(probsPriori: list, matrizCanal: list, probs_salida: list) -> list[list[float]]:
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

matrizCanal = [
    [0.4,0.4,0.2],
    [0.3,0.2,0.5],
    [0.3,0.4,0.3]
]
probsPriori = [0.3, 0.3, 0.4]
salidas = getProbabilidadesSalida(probsPriori, matrizCanal)
probsAPosteriori = getProbabilidadesAPosteriori(probsPriori, matrizCanal, salidas)
simultaneas = getProbabilidadesSimultaneas(probsPriori, matrizCanal)
print("Probabilidades de salida:")
for i, prob in enumerate(salidas):
    print(f"P(salida={i+1}) = {prob:.4f}")
print("Probabilidades a posteriori:")
for j in range(len(probsAPosteriori)):
    for i in range(len(probsAPosteriori[0])):
        print(f"P(entrada={i}, salida={j}) = {probsAPosteriori[j][i]:.4f}")
        
print("Probabilidades simultáneas:")
for i in range(len(simultaneas)):
    for j in range(len(simultaneas[0])):
        print(f"P(entrada={i}, salida={j}) = {simultaneas[i][j]:.4f}")

print("--------------------------------------------------------")
print("Ejercicio 8")
'''
Obtener las probabilidades de los símbolos de salida de los canales propuestos en los
ejercicios 1 y 3. Comparar los resultados obtenidos de dos maneras distintas: a partir de
las secuencias de salida y utilizando las probabilidades a priori y la matriz del canal.
'''
entradaEj1 = "abcacaabbcacaabcacaaabcaca"
salidaEj1 = "01010110011001000100010011"

entradaEj3_1 = "1101011001101010010101010100011111"
salidaEj3_1 = "1001111111100011101101010111110110"
entradaEj3_2 = "110101100110101100110101100111110011"
salidaEj3_2 = "110021102110022010220121122100112011"

probsSalidaEj1_msg = getProbabilidadesSalidaConMsg(entradaEj1, salidaEj1)
probsSalidaEj1Calc = getProbabilidadesSalida(ut.getAlfabetoyProbabilidades(entradaEj1)[1], getMatrizCanal(entradaEj1, salidaEj1))

print("Probabilidades de salida del Ejercicio 1:")
for i in range(len(probsSalidaEj1_msg)):
    print(f"P(salida={i}) con mensaje = {probsSalidaEj1_msg[i]:.4f}, calculada = {probsSalidaEj1Calc[i]:.4f}")
    
probsSalidaEj3_1_msg = getProbabilidadesSalidaConMsg(entradaEj3_1, salidaEj3_1)
probsSalidaEj3_1Calc = getProbabilidadesSalida(ut.getAlfabetoyProbabilidades(entradaEj3_1)[1], getMatrizCanal(entradaEj3_1, salidaEj3_1))
print("\nProbabilidades de salida del Ejercicio 3 - Canal 1:")
for i in range(len(probsSalidaEj3_1_msg)):
    print(f"P(salida={i}) con mensaje = {probsSalidaEj3_1_msg[i]:.4f}, calculada = {probsSalidaEj3_1Calc[i]:.4f}")

probsSalidaEj3_2_msg = getProbabilidadesSalidaConMsg(entradaEj3_2, salidaEj3_2)
probsSalidaEj3_2Calc = getProbabilidadesSalida(ut.getAlfabetoyProbabilidades(entradaEj3_2)[1], getMatrizCanal(entradaEj3_2, salidaEj3_2))
print("\nProbabilidades de salida del Ejercicio 3 - Canal 2:")
for i in range(len(probsSalidaEj3_2_msg)):
    print(f"P(salida={i}) con mensaje = {probsSalidaEj3_2_msg[i]:.4f}, calculada = {probsSalidaEj3_2Calc[i]:.4f}")
    
    
print("--------------------------------------------------------")

'''
Ejercicio 11
Desarrollar una función en Python que reciba como parámetros: una lista con las
probabilidades a priori y la matriz de probabilidades condicionales del canal, y retorne una
lista con las entropías a posteriori.
'''

def getEntropiasAPosteriori(probsPriori: list, matrizCanal: list) -> list:
    probsAPosteriori = getProbabilidadesAPosteriori(probsPriori, matrizCanal, getProbabilidadesSalida(probsPriori, matrizCanal))
    num_simbolos_salida = len(matrizCanal[0])
    entropias_posteriori = [0.0] * num_simbolos_salida
    for j in range(num_simbolos_salida):
        entropia = 0.0
        for i in range(len(probsPriori)):
            p = probsAPosteriori[j][i]
            if p > 0:
                entropia += p * math.log2(1/p)
        entropias_posteriori[j] = entropia
    return entropias_posteriori

print("Ejercicio 12")
'''
12. Obtener las entropías a priori y a posteriori de los canales de los ejercicios 1, 3 y 6.
'''
entradaEj1 = "abcacaabbcacaabcacaaabcaca"
salidaEj1 = "01010110011001000100010011"


matrizCanal_ej1 = getMatrizCanal(entradaEj1, salidaEj1)
probsPriori_ej1 = ut.getAlfabetoyProbabilidades(entradaEj1)[1]
entropias_posteriori_ej1 = getEntropiasAPosteriori(probsPriori_ej1, matrizCanal_ej1)
entropiaPriori_ej1 = ut.getEntropia(probsPriori_ej1)
print(f"Entropía a priori del Ejercicio 1: H(entrada) = {entropiaPriori_ej1:.4f}")
print("Entropías a posteriori del Ejercicio 1:")
for i in range(len(entropias_posteriori_ej1)):
    print(f"H(salida={i}) = {entropias_posteriori_ej1[i]:.4f}")
    
entradaEj3_1 = "1101011001101010010101010100011111"
salidaEj3_1 = "1001111111100011101101010111110110"
entradaEj3_2 = "110101100110101100110101100111110011"
salidaEj3_2 = "110021102110022010220121122100112011"

matrizCanal_ej3_1 = getMatrizCanal(entradaEj3_1, salidaEj3_1)
probsPriori_ej3_1 = ut.getAlfabetoyProbabilidades(entradaEj3_1)[1]
entropias_posteriori_ej3_1 = getEntropiasAPosteriori(probsPriori_ej3_1, matrizCanal_ej3_1)
entropiaPriori_ej3_1 = ut.getEntropia(probsPriori_ej3_1)
print(f"\nEntropía a priori del Ejercicio 3 - Canal 1: H(entrada) = {entropiaPriori_ej3_1:.4f}")
print("Entropías a posteriori del Ejercicio 3 - Canal 1:")
for i in range(len(entropias_posteriori_ej3_1)):
    print(f"H(salida={i}) = {entropias_posteriori_ej3_1[i]:.4f}")
matrizCanal_ej3_2 = getMatrizCanal(entradaEj3_2, salidaEj3_2)
probsPriori_ej3_2 = ut.getAlfabetoyProbabilidades(entradaEj3_2)[1]
entropias_posteriori_ej3_2 = getEntropiasAPosteriori(probsPriori_ej3_2, matrizCanal_ej3_2)
entropiaPriori_ej3_2 = ut.getEntropia(probsPriori_ej3_2)
print(f"\nEntropía a priori del Ejercicio 3 - Canal 2: H(entrada) = {entropiaPriori_ej3_2:.4f}")
print("Entropías a posteriori del Ejercicio 3 - Canal 2:")
for i in range(len(entropias_posteriori_ej3_2)):
    print(f"H(salida={i}) = {entropias_posteriori_ej3_2[i]:.4f}")
    
print("-------------------------------------------------------")
print("Ejercicio 13")
'''
Calcular las entropías a priori y a posteriori de los siguientes canales:
C1 = { 0.14, 0.52, 0.34 }
Matriz C1 =
[0.5,0.3,0.2]
[0.0,0.4,0.6]
[0.2,0.8,0.0]

C2 = { 0.25, 0.25, 0.5 }
Matriz C2 =
[0.25,0.25,0.25,0.25]
[0.25,0.25,0.00,0.50]
[0.50,0.00,0.50,0.00]

C3 = { 0.12, 0.24, 0.14, 0.50 }
Matriz C3 =
[0.25,0.15,0.30,0.30]
[0.23,0.27,0.25,0.25]
[0.10,0.40,0.25,0.25]
[0.34,0.26,0.20,0.20]
'''

probsPrioriC1 = [0.14, 0.52, 0.34]
matrizC1 = [
    [0.5, 0.3, 0.2],
    [0.0, 0.4, 0.6],
    [0.2, 0.8, 0.0]
]
entropiaPrioriC1 = ut.getEntropia(probsPrioriC1)
entropias_posterioriC1 = getEntropiasAPosteriori(probsPrioriC1, matrizC1)
print(f"Entropía a priori del Canal C1: H(entrada) = {entropiaPrioriC1:.4f}")
print("Entropías a posteriori del Canal C1:")
for i in range(len(entropias_posterioriC1)):
    print(f"H(salida={i}) = {entropias_posterioriC1[i]:.4f}")
    
probsPrioriC2 = [0.25, 0.25, 0.5]
matrizC2 = [
    [0.25, 0.25, 0.25, 0.25],
    [0.25, 0.25, 0.00, 0.50],
    [0.50, 0.00, 0.50, 0.00]
]
entropiaPrioriC2 = ut.getEntropia(probsPrioriC2)
entropias_posterioriC2 = getEntropiasAPosteriori(probsPrioriC2, matrizC2)
print(f"Entropía a priori del Canal C2: H(entrada) = {entropiaPrioriC2:.4f}")
print("Entropías a posteriori del Canal C2:")
for i in range(len(entropias_posterioriC2)):
    print(f"H(salida={i}) = {entropias_posterioriC2[i]:.4f}")
    
probsPrioriC3 = [0.12, 0.24, 0.14, 0.50]
matrizC3 = [
    [0.25, 0.15, 0.30, 0.30],
    [0.23, 0.27, 0.25, 0.25],
    [0.10, 0.40, 0.25, 0.25],
    [0.34, 0.26, 0.20, 0.20]
]
entropiaPrioriC3 = ut.getEntropia(probsPrioriC3)
entropias_posterioriC3 = getEntropiasAPosteriori(probsPrioriC3, matrizC3)
print(f"Entropía a priori del Canal C3: H(entrada) = {entropiaPrioriC3:.4f}")
print("Entropías a posteriori del Canal C3:")
for i in range(len(entropias_posterioriC3)):
    print(f"H(salida={i}) = {entropias_posterioriC3[i]:.4f}")
    
print("-------------------------------------------------------")
print("Ejercicio 14")
'''
Dados los siguientes canales:
Canal 1:
C1 = { 0.7, 0.3 }
Matriz C1 =
[0.7,0.3]
[0.4,0.6]

Canal 2:
C2 = { 0.5, 0.5 }
Matriz C2 =
[0.3,0.3,0.4]
[0.3,0.3,0.4]

Canal 3:
C3 = { 0.25, 0.5, 0.25 }
Matriz C3 =
[1.0,0.0,0.0,0.0]
[0.0,0.5,0.5,0.0]
[0.0,0.0,0.0,1.0]

Canal 4:
C4 = { 0.25, 0.25, 0.25, 0.25 }
Matriz C4 =
 [1.0,0.0,0.0]
 [0.0,1.0,0.0]
 [0.0,1.0,0.0]
 [0.0,0.0,1.0]
a. Determinar la entropía a priori y la de la salida
b. Obtener la equivocación o ruido y la pérdida
c. Calcular la entropía afín a través de sus relaciones
d. Verificar la reciprocidad de la información mutua
e. Analizar los resultados obtenidos en cada caso
'''

def getEquivocacionRuido(probsPriori: list, matrizCanal: list) -> float:
    """
    Calcula la equivocación (ruido) H(X|Y) por definición.
    
    Definición:
    H(X|Y) = sum_y P(y) * H(X|y)
    donde H(X|y) = + sum_x P(x|y) * log2(1/P(x|y))
    
    Returns:
        float: El valor de la equivocación H(X|Y) en bits.
    """
       
    # --- 2. Calcular Probabilidad de Salida P(Y) ---
    p_y = getProbabilidadesSalida(probsPriori, matrizCanal)
    
    # --- 3. Calcular Probabilidad "Backward" P(X|Y) ---
    probsPosteriori = getProbabilidadesAPosteriori(probsPriori, matrizCanal, p_y)
    
    # --- 4. Calcular P(x,y) ---
    matrizSimultaneas = getProbabilidadesSimultaneas(probsPriori, matrizCanal)
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

def getEntropiaAfín(probsPriori: list[float], matrizCanal: list[list[float]]) -> float:
    matrizSimultaneas = getProbabilidadesSimultaneas(probsPriori, matrizCanal)
    entropiaAfin = 0.0
    for i in range(len(matrizSimultaneas)):
        for j in range(len(matrizSimultaneas[0])):
            entropiaAfin += matrizSimultaneas[i][j] * math.log2(1/matrizSimultaneas[i][j]) if matrizSimultaneas[i][j] > 0 else 0.0
    return entropiaAfin

def getInformacionMutua(probsPriori: list[float], matrizCanal: list[list[float]]) -> float:
    entropiaPriori = ut.getEntropia(probsPriori)
    
    probsSalida = getProbabilidadesSalida(probsPriori, matrizCanal)
    entropiaSalida = ut.getEntropia(probsSalida)
    
    equivocacion = getEquivocacionRuido(probsPriori, matrizCanal)
    perdida = getPerdida(probsPriori, matrizCanal)
    
    informacionMutua1 = entropiaPriori - equivocacion # H(X) - H(X|Y)
    informacionMutua2 = entropiaSalida - perdida # H(Y) - H(Y|X)
    
    assert abs(informacionMutua1 - informacionMutua2) < 1e-6, "La información mutua calculada por ambos métodos no coincide."
    
    return informacionMutua1

probsPrioriC1 = [0.7, 0.3]
matrizC1 = [
    [0.7, 0.3],
    [0.4, 0.6]
]
entropiaPrioriC1 = ut.getEntropia(probsPrioriC1)
probsSalidaC1 = getProbabilidadesSalida(probsPrioriC1, matrizC1)
entropiaSalidaC1 = ut.getEntropia(probsSalidaC1)
equivocacionC1 = getEquivocacionRuido(probsPrioriC1, matrizC1)
perdidaC1 = getPerdida(probsPrioriC1, matrizC1)
entropiaAfinC1 = getEntropiaAfín(probsPrioriC1, matrizC1)
informacionMutua = getInformacionMutua(probsPrioriC1, matrizC1)
print(f"Canal 1:")
print(f"  Entropía a priori: H(entrada) = {entropiaPrioriC1:.4f}")
print(f"  Entropía a posteriori: H(salida) = {entropiaSalidaC1:.4f}")
print(f"  Equivocación: E = {equivocacionC1:.4f}")
print(f"  Pérdida: L = {perdidaC1:.4f}")
print(f"  Entropía afín: H_afín = {entropiaAfinC1:.4f}")
print(f"  Información mutua: I = {informacionMutua:.4f}")

probsPrioriC2 = [0.5, 0.5]
matrizC2 = [
    [0.3, 0.3, 0.4],
    [0.3, 0.3, 0.4]
]
entropiaPrioriC2 = ut.getEntropia(probsPrioriC2)
probsSalidaC2 = getProbabilidadesSalida(probsPrioriC2, matrizC2)
entropiaSalidaC2 = ut.getEntropia(probsSalidaC2)
equivocacionC2 = getEquivocacionRuido(probsPrioriC2, matrizC2)
perdidaC2 = getPerdida(probsPrioriC2, matrizC2)
entropiaAfinC2 = getEntropiaAfín(probsPrioriC2, matrizC2)
informacionMutuaC2 = getInformacionMutua(probsPrioriC2, matrizC2)
print(f"\nCanal 2:")
print(f"  Entropía a priori: H(entrada) = {entropiaPrioriC2:.4f}")
print(f"  Entropía a posteriori: H(salida) = {entropiaSalidaC2:.4f}")
print(f"  Equivocación: E = {equivocacionC2:.4f}")
print(f"  Pérdida: L = {perdidaC2:.4f}")
print(f"  Entropía afín: H_afín = {entropiaAfinC2:.4f}")
print(f"  Información mutua: I = {informacionMutuaC2:.4f}")

probsPrioriC3 = [0.25, 0.5, 0.25]
matrizC3 = [
    [1.0, 0.0, 0.0, 0.0],
    [0.0, 0.5, 0.5, 0.0],
    [0.0, 0.0, 0.0, 1.0]
]
entropiaPrioriC3 = ut.getEntropia(probsPrioriC3)
probsSalidaC3 = getProbabilidadesSalida(probsPrioriC3, matrizC3)
entropiaSalidaC3 = ut.getEntropia(probsSalidaC3)
equivocacionC3 = getEquivocacionRuido(probsPrioriC3, matrizC3)
perdidaC3 = getPerdida(probsPrioriC3, matrizC3)
entropiaAfinC3 = getEntropiaAfín(probsPrioriC3, matrizC3)
informacionMutuaC3 = getInformacionMutua(probsPrioriC3, matrizC3)
print(f"\nCanal 3:")
print(f"  Entropía a priori: H(entrada) = {entropiaPrioriC3:.4f}")
print(f"  Entropía a posteriori: H(salida) = {entropiaSalidaC3:.4f}")
print(f"  Equivocación: E = {equivocacionC3:.4f}")
print(f"  Pérdida: L = {perdidaC3:.4f}")
print(f"  Entropía afín: H_afín = {entropiaAfinC3:.4f}")
print(f"  Información mutua: I = {informacionMutuaC3:.4f}")

probsPrioriC4 = [0.25, 0.25, 0.25, 0.25]
matrizC4 = [
    [1.0, 0.0, 0.0],
    [0.0, 1.0, 0.0],
    [0.0, 1.0, 0.0],
    [0.0, 0.0, 1.0]
]
entropiaPrioriC4 = ut.getEntropia(probsPrioriC4)
probsSalidaC4 = getProbabilidadesSalida(probsPrioriC4, matrizC4)
entropiaSalidaC4 = ut.getEntropia(probsSalidaC4)
equivocacionC4 = getEquivocacionRuido(probsPrioriC4, matrizC4)
perdidaC4 = getPerdida(probsPrioriC4, matrizC4)
entropiaAfinC4 = getEntropiaAfín(probsPrioriC4, matrizC4)
informacionMutuaC4 = getInformacionMutua(probsPrioriC4, matrizC4)
print(f"\nCanal 4:")
print(f"  Entropía a priori: H(entrada) = {entropiaPrioriC4:.4f}")
print(f"  Entropía a posteriori: H(salida) = {entropiaSalidaC4:.4f}")
print(f"  Equivocación: E = {equivocacionC4:.4f}")
print(f"  Pérdida: L = {perdidaC4:.4f}")
print(f"  Entropía afín: H_afín = {entropiaAfinC4:.4f}")
print(f"  Información mutua: I = {informacionMutuaC4:.4f}")

print("-------------------------------------------------------")
print("Ejercicio 16")
'''
16. Para los canales de los ejercicios 13 y 14, calcular los siguientes valores y verificar sus
relaciones:
a. Entropía a priori
b. Entropía de la salida
c. Equivocación o ruido
d. Pérdida
e. Entropía afín
f. Información mutua
'''


def verificarRelaciones(probsPriori: list[float], matrizCanal: list[list[float]]) -> bool:
    entropiaPriori = ut.getEntropia(probsPriori)
    probsSalida = getProbabilidadesSalida(probsPriori, matrizCanal)
    entropiaSalida = ut.getEntropia(probsSalida)
    equivocacion = getEquivocacionRuido(probsPriori, matrizCanal)
    perdida = getPerdida(probsPriori, matrizCanal)
    entropiaAfin = getEntropiaAfín(probsPriori, matrizCanal)
    informacionMutua = getInformacionMutua(probsPriori, matrizCanal)

    print(f"Entropía a priori: H(entrada) = {entropiaPriori:.4f}")
    print(f"Entropía de la salida: H(salida) = {entropiaSalida:.4f}")
    print(f"Equivocación (ruido): H(X|Y) = {equivocacion:.4f}")
    print(f"Pérdida: H(Y|X) = {perdida:.4f}")
    print(f"Entropía afín: H_afín = {entropiaAfin:.4f}")
    print(f"Información mutua: I(X;Y) = {informacionMutua:.4f}")
    # Verificar relaciones
    response = True
    
    if entropiaAfin != entropiaPriori + entropiaSalida - informacionMutua:
        print("La relación de la entropía afín no se cumple.")
        response = False

    return response

probsPrioriC1 = [0.14, 0.52, 0.34]
matrizC1 = [
    [0.5, 0.3, 0.2],
    [0.0, 0.4, 0.6],
    [0.2, 0.8, 0.0]
]
entropiaPrioriC1 = ut.getEntropia(probsPrioriC1)
probsSalidaC1 = getProbabilidadesSalida(probsPrioriC1, matrizC1)
entropias_posterioriC1 = ut.getEntropia(probsSalidaC1)
ruidoC1 = getEquivocacionRuido(probsPrioriC1, matrizC1)
perdidaC1 = getPerdida(probsPrioriC1, matrizC1)
entropiaAfinC1 = getEntropiaAfín(probsPrioriC1, matrizC1)
informacionMutuaC1 = getInformacionMutua(probsPrioriC1, matrizC1)
print("Canal C1:")
print(f"  Entropía a priori: H(entrada) = {entropiaPrioriC1:.4f}")
print(f"  Entropía a posteriori: H(salida) = {entropias_posterioriC1:.4f}")
print(f"  Equivocación: E = {ruidoC1:.4f}")
print(f"  Pérdida: L = {perdidaC1:.4f}")
print(f"  Entropía afín: H_afín = {entropiaAfinC1:.4f}")
print(f"  Información mutua: I = {informacionMutuaC1:.4f}")
print("Verificación de relaciones para el Canal C1:", "Correcto" if verificarRelaciones(probsPrioriC1, matrizC1) else "Incorrecto")

probsPrioriC2 = [0.25, 0.25, 0.5]
matrizC2 = [
    [0.25, 0.25, 0.25, 0.25],
    [0.25, 0.25, 0.00, 0.50],
    [0.50, 0.00, 0.50, 0.00]
]
entropiaPrioriC2 = ut.getEntropia(probsPrioriC2)
probsSalidaC2 = getProbabilidadesSalida(probsPrioriC2, matrizC2)
entropias_posterioriC2 = ut.getEntropia(probsSalidaC2)
ruidoC2 = getEquivocacionRuido(probsPrioriC2, matrizC2)
perdidaC2 = getPerdida(probsPrioriC2, matrizC2)
entropiaAfinC2 = getEntropiaAfín(probsPrioriC2, matrizC2)
informacionMutuaC2 = getInformacionMutua(probsPrioriC2, matrizC2)
print("\nCanal C2:")
print(f"  Entropía a priori: H(entrada) = {entropiaPrioriC2:.4f}")
print(f"  Entropía a posteriori: H(salida) = {entropias_posterioriC2:.4f}")
print(f"  Equivocación: E = {ruidoC2:.4f}")
print(f"  Pérdida: L = {perdidaC2:.4f}")
print(f"  Entropía afín: H_afín = {entropiaAfinC2:.4f}")
print(f"  Información mutua: I = {informacionMutuaC2:.4f}")
print("Verificación de relaciones para el Canal C2:", "Correcto" if verificarRelaciones(probsPrioriC2, matrizC2) else "Incorrecto")




probsPrioriC3 = [0.12, 0.24, 0.14, 0.50]
matrizC3 = [
    [0.25, 0.15, 0.30, 0.30],
    [0.23, 0.27, 0.25, 0.25],
    [0.10, 0.40, 0.25, 0.25],
    [0.34, 0.26, 0.20, 0.20]
]

