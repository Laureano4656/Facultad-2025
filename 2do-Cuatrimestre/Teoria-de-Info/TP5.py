
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
    num_columnas = len(simbolos_salida)
    conteo_pares = [[0] * num_columnas for _ in range(num_filas)]

    # Recorrer las secuencias para llenar los contadores
    for i in range(len(entrada)):
        sim_in = entrada[i]
        sim_out = salida[i]

        # Incrementar el conteo total del símbolo de entrada
        conteo_entrada[sim_in] += 1
        
        # Incrementar el conteo del par (entrada, salida)
        idx_fila = mapa_entrada[sim_in]
        idx_columna = mapa_salida[sim_out]
        conteo_pares[idx_fila][idx_columna] += 1

    # 3. Calcular probabilidades y construir la matriz final
    matriz_canal = [[0.0] * num_columnas for _ in range(num_filas)]

    for simbolo_in, i in mapa_entrada.items():
        total_apariciones = conteo_entrada[simbolo_in]
        if total_apariciones > 0:
            for j in range(num_columnas):
                matriz_canal[i][j] = conteo_pares[i][j] / total_apariciones
    
    return matriz_canal



# Ejemplo de uso
entrada = "abcacaabbcacaabcacaaabcaca"
salida = "01010110011001000100010011"
matriz_canal = getMatrizCanal(entrada, salida)
for fila in matriz_canal:
    print(fila)

print("--------------------------------------------------------")
print("Ejercicio 3")
'''
Dadas las siguientes secuencias de entrada y sus respectivas salidas, las cuales describen
el comportamiento de los canales, calcular las probabilidades a priori y la matriz del canal.

'''
entrada1 = "1101011001101010010101010100011111"
salida1 = "1001111111100011101101010111110110"
matriz_canal1 = getMatrizCanal(entrada1, salida1)
probabilidades_entrada1 = ut.getAlfabetoyProbabilidades(entrada1)[1]

print("Canal 1:")
print("Probabilidades a priori de la entrada:")
for simbolo, prob in zip(ut.getAlfabetoyProbabilidades(entrada1)[0], probabilidades_entrada1):
    print(f"Símbolo: {simbolo}, Probabilidad: {prob:.4f}")

print("Matriz del canal:")
for fila in matriz_canal1:
    print(fila)
    
entrada2 = "110101100110101100110101100111110011"
salida2 = "110021102110022010220121122100112011"
matriz_canal2 = getMatrizCanal(entrada2, salida2)
probabilidades_entrada2 = ut.getAlfabetoyProbabilidades(entrada2)[1]
print("\nCanal 2:")
print("Probabilidades a priori de la entrada:")
for simbolo, prob in zip(ut.getAlfabetoyProbabilidades(entrada2)[0], probabilidades_entrada2):
    print(f"Símbolo: {simbolo}, Probabilidad: {prob:.4f}")
print("Matriz del canal:")
for fila in matriz_canal2:
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

def getProbabilidadesSalida(probsPriori: list, matriz_canal: list) -> list:
    num_simbolos_salida = len(matriz_canal[0])
    probs_salida = [0.0] * num_simbolos_salida

    for j in range(num_simbolos_salida):
        for i in range(len(probsPriori)):
            probs_salida[j] += probsPriori[i] * matriz_canal[i][j]

    return probs_salida

def getProbabilidadesSalidaConMsg(entrada: str, salida: str) -> list:
    matriz_canal = getMatrizCanal(entrada, salida)
    probsPriori = ut.getAlfabetoyProbabilidades(entrada)[1]
    num_simbolos_salida = len(matriz_canal[0])
    probs_salida = [0.0] * num_simbolos_salida

    for j in range(num_simbolos_salida):
        for i in range(len(probsPriori)):
            probs_salida[j] += probsPriori[i] * matriz_canal[i][j]

    return probs_salida

def getProbabilidadesSimultaneasConMsg(entrada: str, salida: str) -> list:
    matriz_canal = getMatrizCanal(entrada, salida)
    probsPriori = ut.getAlfabetoyProbabilidades(entrada)[1]
    num_simbolos_salida = len(matriz_canal[0])
    probs_simultaneas = [[0.0] * num_simbolos_salida for _ in range(len(probsPriori))]

    for i in range(len(probsPriori)):
        for j in range(num_simbolos_salida):
            probs_simultaneas[i][j] = probsPriori[i] * matriz_canal[i][j]

    return probs_simultaneas

def getProbabilidadesSimultaneas(probsPriori: list, matriz_canal: list) -> list:
    num_simbolos_salida = len(matriz_canal[0])
    probs_simultaneas = [[0.0] * num_simbolos_salida for _ in range(len(probsPriori))]

    for i in range(len(probsPriori)):
        for j in range(num_simbolos_salida):
            probs_simultaneas[i][j] = probsPriori[i] * matriz_canal[i][j]

    return probs_simultaneas

probsPriori = [0.2, 0.8]
matriz_canal_binario = [[1.0, 0.0], [0.0, 1.0]]  # Canal sin ruido
salidas = getProbabilidadesSalida(probsPriori, matriz_canal_binario)
simultaneas = getProbabilidadesSimultaneas(probsPriori, matriz_canal_binario)
print("Probabilidades de salida con P(0)=0.2 y P(1)=0.8:")
for i, prob in enumerate(salidas):
    print(f"P(salida={i}) = {prob:.4f}")
    
print("Probabilidades simultáneas con P(0)=0.2 y P(1)=0.8:")
for i in range(len(simultaneas)):
    for j in range(len(simultaneas[0])):
        print(f"P(entrada={i}, salida={j}) = {simultaneas[i][j]:.4f}")