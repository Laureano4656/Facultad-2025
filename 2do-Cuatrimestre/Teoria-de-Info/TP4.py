import FuncTeoriaDeLaInfo as ut

'''
Ejercicio 1
'''
#  Codificar una función booleana en Python que reciba como parámetros: una lista con la
# distribución de probabilidades de una fuente, otra lista con palabras código y el orden N de
# la extensión, y verifique si el código cumple con el Primer Teorema de Shannon.

def verificar_primer_teorema(probabilidades, codigo, N):
    # Calcular la entropía de la fuente
    H = ut.getEntropiaCodigoR(codigo,probabilidades)
    
    # Calcular la longitud promedio del código

    probsExtension = ut.probabilidadesOrdenN(probabilidades, N)
    Ln = ut.getLongitudMedia(codigo, probsExtension)

    # Verificar el Primer Teorema de Shannon
    cumple_teorema = H <= Ln / N <= H + (1/N)
    
    return cumple_teorema

'''
Ejercicio 2
'''
print("Ejercicio 2")
# Dada la siguiente fuente de información y su codificación, comprobar si la fuente y su
# extensión de orden 2 cumplen con el Primer Teorema de Shannon

probs = [0.3,0.1,0.4,0.2]
codigo = ['BA', 'CAB', 'A', 'CBA']

cumple = verificar_primer_teorema(probs, codigo, 1)
print(f"¿La fuente original cumple con el Primer Teorema de Shannon? {cumple}")
cumple_extension = verificar_primer_teorema(probs, codigo, 2)
print(f"¿La extensión de orden 2 cumple con el Primer Teorema de Shannon? {cumple_extension}")
print(f"Entropía de la fuente original: {ut.getEntropiaCodigoR(codigo, probs)}")
print(f"Longitud media del código original: {ut.getLongitudMedia(codigo, probs)}")
alfExtension,probsExt  = ut.calcExtensionN(codigo, probs, 2)
print(f"Longitud media del código de la extensión de orden 2: {ut.getLongitudMedia(alfExtension, probsExt)}")

print("---------------------------------------------------------")
'''Ejercicio 3'''
# Si se tiene una fuente de información con probabilidades P = { 0.5, 0.2, 0.3 } y los
# siguientes códigos para la fuente y su extensión de orden 2, verificar el cumplimiento del
# Primer Teorema de Shannon para ambas codificaciones:
# ● C1 = { 11, 010, 00 }
# ● C2 = { 10, 001, 110, 010, 0000, 0001, 111, 0110, 0111 }
print("Ejercicio 3")

probs = [0.5, 0.2, 0.3]
codigo1 = ['11', '010', '00']
cumple_c1 = verificar_primer_teorema(probs, codigo1, 1)
print(f"¿El código C1 cumple con el Primer Teorema de Shannon? {cumple_c1}")
print(f"Entropía de la fuente original: {ut.getEntropiaCodigoR(codigo1, probs)}")
print(f"Longitud media del código original: {ut.getLongitudMedia(codigo1, probs)}")

codigo2 = ['10', '001', '110', '010', '0000', '0001', '111', '0110', '0111']

probsExt2 = ut.probabilidadesOrdenN(probs, 2)

cumple_c2 = verificar_primer_teorema(probs, codigo2, 2)
print(f"¿El código C2 cumple con el Primer Teorema de Shannon? {cumple_c2}")
print(f"Entropía de la fuente de orden 2: {ut.getEntropiaCodigoR(codigo2, probsExt2)}")
print(f"Longitud media del código de la extensión de orden 2: {ut.getLongitudMedia(codigo2, probsExt2)}")

print("---------------------------------------------------------")
'''Ejercicio 5'''
# Para una fuente binaria con ω = 0.7:
# a. Obtener una codificación mediante el algoritmo de Huffman
# b. Codificar la extensión de orden 2 mediante el algoritmo de Shannon-Fano
# c. Comprobar si las codificaciones cumplen con el Primer Teorema de Shannon

def getCodigoHuffman(probs: list) -> list:
    """
    Genera códigos Huffman de forma iterativa utilizando una lista de listas
    para rastrear los símbolos sin construir un árbol explícito.
    """
    # Caso base para listas vacías o con un solo elemento.
    if len(probs) <= 1:
        return [""] * len(probs)

    # 1. INICIALIZACIÓN
    # Cada elemento es [probabilidad, [lista_de_indices_originales]]
    items = [[p, [i]] for i, p in enumerate(probs)]
    
    # Lista final donde se construirán los códigos.
    codigos = [""] * len(probs)

    # 2. BUCLE ITERATIVO
    # El bucle se ejecuta hasta que todos los símbolos se hayan fusionado en uno.
    while len(items) > 1:
        # Ordenamos la lista en cada paso para encontrar los 2 menos probables.
        items.sort(key=lambda item: item[0])
        
        # Extraemos los dos elementos con menor probabilidad.
        grupoMenor = items.pop(0)
        grupoMayor = items.pop(0)
        
        # 3. CONSTRUCCIÓN DE CÓDIGOS
        # A todos los símbolos originales del grupo menor, les añadimos un '0' al inicio.
        for index in grupoMenor[1]:
            codigos[index] = "0" + codigos[index]
            
        # A los del grupo mayor, les añadimos un '1'.
        for index in grupoMayor[1]:
            codigos[index] = "1" + codigos[index]
            
        # 4. COMBINACIÓN
        # Creamos un nuevo "símbolo" fusionado.
        probCombinada = grupoMenor[0] + grupoMayor[0]
        indicesCombinados = grupoMenor[1] + grupoMayor[1]

        # Lo añadimos de nuevo a la lista para la siguiente iteración.
        items.append([probCombinada, indicesCombinados])

    return codigos
# def getCodigoHuffman(probs):
    
#     if len(probs) == 1:
#         return [""]
#     else:
#         probAct = probs.copy()
#         probAct.sort()
#         items = [[p, [i]] for i, p in enumerate(probs)]
#         i1 = items.index()
#         i2 = items.index()
#         probsNuevas = probs.copy()
#         probsNuevas.remove(probAct[i1])
#         probsNuevas.remove(probAct[i2])
#         probsNuevas.append(probAct[i1] + probAct[i2])
#         codigoNuevas = getCodigoHuffman(probsNuevas)
#         c1 = codigoNuevas[-1] + "0"
#         c2 = codigoNuevas[-1] + "1"
#         codigoNuevas.remove(codigoNuevas[-1])
#         codigoNuevas.append(c1)
#         codigoNuevas.append(c2)

#         if i1 < i2:
#             codigoNuevas.insert(i1, codigoNuevas.pop())
#             codigoNuevas.insert(i2, codigoNuevas.pop())
#         else:
#             codigoNuevas.insert(i2, codigoNuevas.pop())
#             codigoNuevas.insert(i1, codigoNuevas.pop())
#         return codigoNuevas


dist_probs = [0.7, 0.3]
codigoHuffman = getCodigoHuffman(dist_probs)
print(f"Código Huffman: {codigoHuffman}")

def getSortedIndex ( P: list ) -> list:
    return sorted([ [pi, i] for i, pi in enumerate(P) ], key=lambda item: item[0], reverse=True)


def propagateSubfix( result: list, P: list[list], fix: str ) -> list:
    for pi, i in P:
        result[i] +=  fix 

def shannonfano ( result: list, P: list  ):
    if len(P) <= 1:
        return

    # calculate split
    total = sum( [ pi for pi, i in P ]) / 2 

    acum = 0
    lastDif = 1 
    splitLocation = -1


    for i, pi in enumerate(P):
        acum += pi[0]

        if acum >= total:
            if min(lastDif, abs(total - acum)) == lastDif:
                splitLocation = i
            else:
                splitLocation = i + 1
            
            firstPart = P[:splitLocation]
            secondPart = P[splitLocation:]

            propagateSubfix( result, firstPart, '1' )
            propagateSubfix( result, secondPart, '0' )

            shannonfano( result, firstPart)
            shannonfano( result, secondPart)

            return
                
        lastDif = total - acum


def getCodigoShannonFano(probs: list) -> list:
    # Caso base: si solo hay un elemento, no hay más divisiones que hacer.
    if len(probs) <= 1:
        return [""]

    # 1. ORDENAR Y PREPARAR DATOS
    # Guardamos cada probabilidad junto a su índice original.
    items = sorted([[p, i] for i, p in enumerate(probs)], reverse=True)
    total = sum(probs)

    # 2. ENCONTRAR EL MEJOR PUNTO DE DIVISIÓN
    mejor_indice = -1
    # La diferencia nunca será mayor que el total.
    mejor_diferencia = float('inf') 

    suma_actual = 0
    # El bucle debe encontrar el mejor índice, no hacer el trabajo recursivo.
    # Iteramos por todos los posibles puntos de corte.
    for i in range(len(items) - 1):
        suma_actual += items[i][0]
        diferencia = abs(suma_actual - (total - suma_actual))
        
        if diferencia < mejor_diferencia:
            mejor_diferencia = diferencia
            mejor_indice = i + 1 # El corte es DESPUÉS del elemento 'i'
    
    # 3. DIVIDIR Y HACER LAS LLAMADAS RECURSIVAS (FUERA DEL BUCLE)
    grupo1 = items[:mejor_indice]
    grupo2 = items[mejor_indice:]

    # Extraemos las probabilidades para las llamadas recursivas
    probs1 = [item[0] for item in grupo1]
    probs2 = [item[0] for item in grupo2]

    # Llamadas recursivas para los subgrupos
    codigos1 = getCodigoShannonFano(probs1)
    codigos2 = getCodigoShannonFano(probs2)
    
    codigos1 = ["1"+c  for c in codigos1]
    codigos2 = ["0"+c for c in codigos2]

    # Añadimos '0' y '1' a los códigos resultantes

    # 4. RECONSTRUIR EL RESULTADO EN EL ORDEN ORIGINAL
    resultado = [""] * len(probs)
    for i, item in enumerate(grupo1):
        resultado[item[1]] = codigos1[i]
    for i, item in enumerate(grupo2):
        resultado[item[1]] = codigos2[i] 
        
    return resultado

# Ejemplo de uso
probs_ejemplo_franco = [0.2, 0.27, 0.4, 0.13]
codigos_correctos = getCodigoShannonFano(probs_ejemplo_franco)
print(f"Probabilidades: {probs_ejemplo_franco}")
print(f"Códigos generados: {codigos_correctos}")
print(f"Debe ser:  ['001', '01', '1', '000']")

probs_ejemplo_teoria = [0.4, 0.2,0.15,0.1,0.06,0.04,0.03,0.02]
codigos_teoria = getCodigoShannonFano(probs_ejemplo_teoria)
print(f"Probabilidades: {probs_ejemplo_teoria}")
R = ['']*8
decreasingP = getSortedIndex(probs_ejemplo_teoria)
shannonfano(R, decreasingP)
print(f"Códigos generados implementacion valen: {R}")
print(f"Codigos generados mi implementacion: {codigos_teoria}")
print(f"Debe ser:  ['11', '10', '011', '010', '0011', '0010', '0001', '0000']")

print("Huffman cumple con el Primer Teorema de Shannon?")
cumple_huffman = verificar_primer_teorema(dist_probs, codigoHuffman, 1)
print(cumple_huffman)
print("Shannon-Fano cumple con el Primer Teorema de Shannon para la extensión de orden 2?")
probsExt2 = ut.probabilidadesOrdenN(dist_probs, 2)
cumple_shannon_fano = verificar_primer_teorema(probsExt2, codigo2, 2)
print(cumple_shannon_fano)



''' 
6. Realizar una función en Python que reciba como parámetros: dos listas paralelas con la
distribución de probabilidades de una fuente y su codificación, y calcule el rendimiento y la
redundancia del código.
'''
print("Ejercicio 6")
def calcularRendimiento(probabilidades, codigo):
    H = ut.getEntropiaCodigoR(codigo,probabilidades)
    L = ut.getLongitudMedia(codigo,probabilidades)
    R = H / L if L != 0 else 0
    D = 1 - R
    return R

def calcularRedundancia(probabilidades, codigo):
    H = ut.getEntropiaCodigoR(codigo,probabilidades)
    L = ut.getLongitudMedia(codigo,probabilidades)
    R = H / L if L != 0 else 0
    D = 1 - R
    return D

print("---------------------------------------------------------")
print("Ejercicio 7")
'''
7. Comparar los rendimientos y las redundancias de los códigos del ejercicio 3.
'''

probs = [0.5, 0.2, 0.3]
codigo1 = ['11', '010', '00']
R1 = calcularRendimiento(probs, codigo1)
D1 = calcularRedundancia(probs, codigo1)
print(f"Código C1: {codigo1}")
print(f"Rendimiento C1: {R1}")
print(f"Redundancia C1: {D1}")
codigo2 = ['10', '001', '110', '010', '0000', '0001', '111', '0110', '0111']
probsExt2 = ut.probabilidadesOrdenN(probs, 2)
R2 = calcularRendimiento(probsExt2, codigo2)
D2 = calcularRedundancia(probsExt2, codigo2)
print(f"Código C2: {codigo2}")
print(f"Rendimiento C2: {R2}")
print(f"Redundancia C2: {D2}")

print("---------------------------------------------------------")
print("Ejercicio 8")
'''
8. Comparar los rendimientos y las redundancias de los siguientes códigos.
'''
probs = [0.2, 0.15, 0.1, 0.3, 0.25]
codigoA = ['01', '111', '110', '101', '100']
codigoB = ['00', '01', '10', '110', '111']
codigoC = ['0110', '010', '0111', '1', '00']
codigoD = ['11', '001', '000', '10', '01']

R_A = calcularRendimiento(probs, codigoA)
D_A = calcularRedundancia(probs, codigoA)
print(f"Código A: {codigoA}")
print(f"Rendimiento A: {R_A}")
print(f"Redundancia A: {D_A}")

R_B = calcularRendimiento(probs, codigoB)
D_B = calcularRedundancia(probs, codigoB)
print(f"Código B: {codigoB}")
print(f"Rendimiento B: {R_B}")
print(f"Redundancia B: {D_B}")

R_C = calcularRendimiento(probs, codigoC)
D_C = calcularRedundancia(probs, codigoC)
print(f"Código C: {codigoC}")
print(f"Rendimiento C: {R_C}")
print(f"Redundancia C: {D_C}")

R_D = calcularRendimiento(probs, codigoD)
D_D = calcularRedundancia(probs, codigoD)
print(f"Código D: {codigoD}")
print(f"Rendimiento D: {R_D}")
print(f"Redundancia D: {D_D}")

print("---------------------------------------------------------")
print("Ejercicio 9")
'''
9. Dadas las siguientes fuentes, generar códigos de Huffman y de Shannon-Fano:
'''
probsA = [0.2,0.2,0.3,0.3]
probsB = [0.4,0.25,0.25,0.1]

codigoA = getCodigoHuffman(probsA)
print(f"Código Huffman A: {codigoA}")
codigoB = getCodigoHuffman(probsB)
print(f"Código Huffman B: {codigoB}")
codigoA_sf = getCodigoShannonFano(probsA)
print(f"Código Shannon-Fano A: {codigoA_sf}")
codigoB_sf = getCodigoShannonFano(probsB)
print(f"Código Shannon-Fano B: {codigoB_sf}")

print("---------------------------------------------------------")
print("Ejercicio 10")
'''
10. Construir códigos de Huffman y de Shannon-Fano para fuentes de información que emiten
los siguientes mensajes representativos:.
'''
msgA = "ABCDABCBDCBAAABBBCBCBABADBCBABCBDBCCCAAABB"
msgB = "AOEAOEOOOOEOAOEOOEOOEOAOAOEOEUUUIEOEOEO"

_,probsA = ut.getAlfabetoyProbabilidades(msgA)
_,probsB = ut.getAlfabetoyProbabilidades(msgB)

codigoA_huff = getCodigoHuffman(probsA)
print(f"Código Huffman A: {codigoA_huff}")
codigoB_huff = getCodigoHuffman(probsB)
print(f"Código Huffman B: {codigoB_huff}")
codigoA_sf = getCodigoShannonFano(probsA)
print(f"Código Shannon-Fano A: {codigoA_sf}")
codigoB_sf = getCodigoShannonFano(probsB)
print(f"Código Shannon-Fano B: {codigoB_sf}")

print("---------------------------------------------------------")
print("Ejercicio 12")
'''
12. Para una fuente de información con distribución de probabilidades:
P = { 0.385, 0.154, 0.128, 0.154, 0.179 }
a. Calcular la entropía de la fuente
b. Generar una codificación de Huffman
c. Obtener una codificación de Shannon-Fano
d. Graficar los árboles binarios que surgen de cada codificación
e. Comparar la longitud media, el rendimiento y la redundancia de cada código
'''

probs = [0.385, 0.154, 0.128, 0.154, 0.179]

H = ut.getEntropia(probs)
codHuffman = getCodigoHuffman(probs)
codShannonFano = getCodigoShannonFano(probs)

L_huff = ut.getLongitudMedia(codHuffman, probs)
R_huff = calcularRendimiento(probs, codHuffman)
D_huff = calcularRedundancia(probs, codHuffman)

L_sf = ut.getLongitudMedia(codShannonFano, probs)
R_sf = calcularRendimiento(probs, codShannonFano)
D_sf = calcularRedundancia(probs, codShannonFano)
print(f"Entropía de la fuente: {H}")
print(f"Código Huffman: {codHuffman}")
print(f"Longitud media Huffman: {L_huff}")
print(f"Rendimiento Huffman: {R_huff}")
print(f"Redundancia Huffman: {D_huff}")
print(f"Código Shannon-Fano: {codShannonFano}")
print(f"Longitud media Shannon-Fano: {L_sf}")
print(f"Rendimiento Shannon-Fano: {R_sf}")
print(f"Redundancia Shannon-Fano: {D_sf}")

print("---------------------------------------------------------")
print("Ejercicio 13")
'''
13. Dada una fuente de información que emite el siguiente mensaje representativo:
58784784525368669895745123656253698989656452121702300223659
a. Calcular la entropía de la fuente
b. Construir una codificación de Huffman
c. Generar una codificación de Shannon-Fano
d. Comparar la longitud media, el rendimiento y la redundancia de cada código
'''

msg = "58784784525368669895745123656253698989656452121702300223659"
_,probs = ut.getAlfabetoyProbabilidades(msg)

H = ut.getEntropia(probs)
codHuffman = getCodigoHuffman(probs)
codShannonFano = getCodigoShannonFano(probs)

L_huff = ut.getLongitudMedia(codHuffman, probs)
R_huff = calcularRendimiento(probs, codHuffman)
D_huff = calcularRedundancia(probs, codHuffman)

L_sf = ut.getLongitudMedia(codShannonFano, probs)
R_sf = calcularRendimiento(probs, codShannonFano)
D_sf = calcularRedundancia(probs, codShannonFano)
print(f"Entropía de la fuente: {H}")
print(f"Código Huffman: {codHuffman}")
print(f"Longitud media Huffman: {L_huff}")
print(f"Rendimiento Huffman: {R_huff}")
print(f"Redundancia Huffman: {D_huff}")
print(f"Código Shannon-Fano: {codShannonFano}")
print(f"Longitud media Shannon-Fano: {L_sf}")
print(f"Rendimiento Shannon-Fano: {R_sf}")
print(f"Redundancia Shannon-Fano: {D_sf}")

print("---------------------------------------------------------")

'''
14. De acuerdo a la codificación del ejercicio 2, decodificar los siguientes mensajes:
a. ABACBAACABABAACBABA
b. BACBAAABAAACBABACAB
c. CBAABACBABAAACABABA
'''
print("Ejercicio 15")
'''
15. Implementar funciones en Python que reciban como parámetros: una cadena de
caracteres que contenga un alfabeto fuente y una lista de cadenas de caracteres que
almacena una codificación en el alfabeto binario, y resuelvan lo siguiente:
a. Dada una cadena de caracteres con un mensaje escrito en el alfabeto fuente,
devolver una secuencia de bytes (bytearray) que contenga el mensaje codificado.
b. Dada una secuencia de bytes, decodificar y retornar el mensaje original.
Sugerencia: manipular el mensaje codificado como una cadena de caracteres de unos y
ceros, tanto para codificar como para decodificar, y realizar las conversiones entre binarios
y enteros con las funciones de casteo correspondientes
'''

def codeMessage(codigo: list, mensaje: str,alfabeto = [],) -> bytearray:
    if not len(alfabeto) :
        alfabeto, _ = ut.getAlfabetoyProbabilidades(mensaje)
    # Crear un diccionario para mapear cada símbolo a su código binario
    codigoDict = {alfabeto[i]: codigo[i] for i in range(len(alfabeto))}
    
    # Codificar el mensaje
    mensajeCodificado = ''.join(codigoDict[char] for char in mensaje)
    longitudMsgCodificado = len(mensajeCodificado)
        
    bitsRelleno = 0
    while longitudMsgCodificado % 8 != 0:
        mensajeCodificado += '0'  # Rellenar con ceros a la derecha
        bitsRelleno += 1
        longitudMsgCodificado += 1

    # Convertir la cadena de bits en un bytearray
    byte_array = bytearray()
    byte_array.append(bitsRelleno)  # Primer byte indica la cantidad de bits de relleno
    for i in range(0, len(mensajeCodificado), 8):
        byte_segment = mensajeCodificado[i:i+8]
        byte_array.append(int(byte_segment, 2))  # Rellenar con ceros a la derecha si es necesario
    
    return byte_array

def decodeMessage(alfabeto: list, codigo: list, byte_array: bytearray) -> str:
    
    # Crear un diccionario para mapear cada código binario a su símbolo
    codigoDict = {codigo[i]: alfabeto[i] for i in range(len(alfabeto))}
    
    # Convertir el bytearray de nuevo a una cadena de bits
    mensajeCodificado = ''.join(f'{byte:08b}' for byte in byte_array)
    bitsRelleno = int(mensajeCodificado[:8], 2)  # Primer byte indica la cantidad de bits de relleno
    mensajeCodificado = mensajeCodificado[8:]  # Eliminar el byte de relleno
    if bitsRelleno > 0:
        mensajeCodificado = mensajeCodificado[:-bitsRelleno]  # Eliminar los bits de relleno al final
    # Decodificar el mensaje
    mensajeDecodificado = ''
    temp = ''
    for bit in mensajeCodificado:
        temp += bit
        if temp in codigoDict:
            mensajeDecodificado += codigoDict[temp]
            temp = ''
    
    return mensajeDecodificado

msg = "Hola mundo penso"
_ , probs = ut.getAlfabetoyProbabilidades(msg)
codigo = getCodigoHuffman(probs)  # Ejemplo de código para H, o, l, a, espacio, m, u, n, d
codedMessage = codeMessage(codigo, msg)
print(f"Mensaje codificado: {codedMessage}")
decodedMessage = decodeMessage(ut.getAlfabetoyProbabilidades(msg)[0], codigo, codedMessage)
print(f"Mensaje decodificado: {decodedMessage}")

print("---------------------------------------------------------")
print("Ejercicio 16")
'''
Ejercicio 16
Codificar una función en Python que reciba como parámetros: una cadena de caracteres
con un mensaje y una secuencia de bytes (bytearray) con ese mensaje codificado y calcule
la tasa de compresión.

'''
def calcularTasaCompresion(mensaje: str, mensajeCodificado: bytearray) -> float:
    # Calcular el tamaño del mensaje original en bits
    originalSize = len(mensaje) * 8  # Cada carácter se asume que ocupa 8 bits
    residuo = mensajeCodificado[0]  # Primer byte indica la cantidad de bits de relleno
    # Calcular el tamaño del mensaje codificado en bits
    print(f"Bits de relleno: {residuo}")
    codedSize = (len(mensajeCodificado) * 8)   # Cada byte en el bytearray ocupa 8 bits
    
    #codedSize -=  residuo  # Restar los bits de relleno
    # Calcular la tasa de compresión
    if codedSize == 0:
        return 0.0  # Evitar división por cero si el mensaje codificado está vacío
    tasaCompresion = originalSize / codedSize
    
    return tasaCompresion


print("------------------------------------------------------")
print("Ejercicio 17")

'''
Dada la siguiente tabla de probabilidades:
Utilizando las funciones desarrolladas en los ejercicios 11 y 15, comprimir un mensaje
mediante el algoritmo de Huffman y/o Shannon-Fano y almacenarlo en un archivo binario.
Enviar el archivo a un compañero, quien tendrá que extraer y descomprimir el mensaje.
Ambos deben calcular la tasa de compresión, el rendimiento y la redundancia.
'''

def createFile(name: str, byte_array: bytearray):
    with open(name, 'wb') as file:
        file.write(byte_array)

def readFile(name: str) -> bytearray:
    with open(name, 'rb') as file:
        byte_array = bytearray(file.read())
    return byte_array

alfabeto = [
  " ", ",", ".", ":", ";", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K",
  "L", "M", "N", "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
]

probs = [
  0.175990, 0.014093, 0.015034, 0.000542, 0.002109, 0.111066, 0.015368, 0.030176,
  0.038747, 0.101604, 0.004873, 0.008762, 0.007953, 0.049740, 0.003706, 0.000034,
  0.048149, 0.021041, 0.050490, 0.002018, 0.073793, 0.019583, 0.010246, 0.051446,
  0.058406, 0.031093, 0.033240, 0.008930, 0.000012, 0.000706, 0.007851, 0.003199,
]

mensaje = "RESPETO MAXIMO"

codigoHuffman = getCodigoHuffman(probs)
byteArrayMsg = codeMessage(codigoHuffman, mensaje, alfabeto)
createFile("mensaje_codificado.bin", byteArrayMsg)

tasaCompresion = calcularTasaCompresion(mensaje, byteArrayMsg)
R = calcularRendimiento(probs, codigoHuffman)
D = calcularRedundancia(probs, codigoHuffman)

byteArrayRead = readFile("mensaje_codificado.bin")
mensajeDecodificado = decodeMessage(alfabeto, codigoHuffman, byteArrayRead)


print(f"Tasa de compresión: {tasaCompresion}")
print(f"Rendimiento del código: {R}")
print(f"Redundancia del código: {D}")

print(f"Mensaje decodificado: {mensajeDecodificado}")

print("------------------------------------------------------")
print("Ejercicio 18")
'''
18. Comprimir los siguientes mensajes utilizando el algoritmo RLC:
a. XXXYZZZZ
b. AAAABBBCCDAA
c. UUOOOOAAAIEUUUU
'''
msg1 = "XXXYZZZZ"
msg2 = "AAAABBBCCDAA"
msg3 = "UUOOOOAAAIEUUUU"

def compressRLC(mensaje: str) -> list:
    if not mensaje:
        return []
    
    compressed = ""
    count = 1
    prev_char = mensaje[0]
    
    for char in mensaje[1:]:
        if char == prev_char:
            count += 1
        else:
            compressed += f"{prev_char}{count}"
            prev_char = char
            count = 1
    compressed += f"{prev_char}{count}"  # Añadir el último grupo

    return compressed

print(f"Mensaje: {msg1} -> Comprimido RLC: {compressRLC(msg1)}")
print(f"Mensaje: {msg2} -> Comprimido RLC: {compressRLC(msg2)}")
print(f"Mensaje: {msg3} -> Comprimido RLC: {compressRLC(msg3)}")

print("------------------------------------------------------")
print("Ejercicio 19")
'''
Realizar una función en Python que reciba como parámetro una cadena de caracteres con
un mensaje y devuelva una secuencia de bytes (bytearray) que contenga el mensaje
comprimido con RLC, utilizando un byte para almacenar la representación en código ASCII
del carácter y otro byte para el número.

'''

def compressRLCToBytes(mensaje: str) -> bytearray:
    if not mensaje:
        return bytearray()

    count = 1
    prev_char = mensaje[0]
    longitudMsg = len(mensaje)
    bitsRelleno = 0
    
    while longitudMsg % 8 != 0:
        mensaje += '0'  # Rellenar con ceros a la derecha
        bitsRelleno += 1
        longitudMsg += 1
        
    compressed = bytearray()

    compressed.append(bitsRelleno)  # Primer byte indica la cantidad de bits de relleno
    
    for char in mensaje[1:]:
        if char == prev_char:
            count += 1
        else:
            compressed.append(ord(prev_char))
            compressed.append(count)
            prev_char = char
            count = 1

    compressed.append(ord(prev_char))
    compressed.append(count)

    return compressed

print("------------------------------------------------------")
print("Ejercicio 20")
'''
Volver a comprimir los mensajes del ejercicio 18 (utilizando la función desarrollada) y
calcular la tasa de compresión de cada uno.
'''
msg1 = "XXXYZZZZ"
msg2 = "AAAABBBCCDAA"
msg3 = "UUOOOOAAAIEUUUU"

byteArrayMsg1 = compressRLCToBytes(msg1)
tasaCompresion1 = calcularTasaCompresion(msg1, byteArrayMsg1)
print(f"Mensaje: {msg1} ->  Tasa de compresión: {tasaCompresion1}")

byteArrayMsg2 = compressRLCToBytes(msg2)
tasaCompresion2 = calcularTasaCompresion(msg2, byteArrayMsg2)
print(f"Mensaje: {msg2} ->  Tasa de compresión: {tasaCompresion2}")

byteArrayMsg3 = compressRLCToBytes(msg3)
tasaCompresion3 = calcularTasaCompresion(msg3, byteArrayMsg3)
print(f"Mensaje: {msg3} ->  Tasa de compresión: {tasaCompresion3}")

print("------------------------------------------------------")
print("Ejercicio 21 y 22")
'''
Dados los siguientes codigos:
C1 = { 00, 01, 10, 11 }
C2 = { 000, 100, 101, 111 }
C3 = { 0000, 0011, 1010, 0101 }
a. Calcular la distancia de Hamming de cada código
b. Determinar para cada código cúantos errores se pueden detectar y corregir
'''
def distanciaHamming(codigo: list) -> int:
    min_distance = float('inf')
    n = len(codigo)
    
    for i in range(n):
        for j in range(i + 1, n):
            # Calcular la distancia de Hamming entre codigo[i] y codigo[j]
            dist = sum(c1 != c2 for c1, c2 in zip(codigo[i], codigo[j]))
            if dist < min_distance:
                min_distance = dist
                
    return min_distance

def erroresDetectables(codigo: list) -> int:
    dist = distanciaHamming(codigo)
    # La cantidad de errores detectables es (d - 1)
    return dist - 1

def erroresCorregibles(codigo: list) -> int:
    dist = distanciaHamming(codigo)
    # La cantidad de errores corregibles es (d - 1) // 2
    return (dist - 1) // 2
codigo1 = ['00', '01', '10', '11']
codigo2 = ['000', '100', '101', '111']
codigo3 = ['0000', '0011', '1010', '0101']

print(f"Código C1: {codigo1}")
print(f"Distancia de Hamming C1: {distanciaHamming(codigo1)}")
print(f"Código C1 puede detectar {erroresDetectables(codigo1)} errores y corregir {erroresCorregibles(codigo1)} errores.")
print(f"Código C2: {codigo2}")
print(f"Distancia de Hamming C2: {distanciaHamming(codigo2)}")
print(f"Código C2 puede detectar {erroresDetectables(codigo2)} errores y corregir {erroresCorregibles(codigo2)} errores.")
print(f"Código C3: {codigo3}")
print(f"Distancia de Hamming C3: {distanciaHamming(codigo3)}")
print(f"Código C3 puede detectar {erroresDetectables(codigo3)} errores y corregir {erroresCorregibles(codigo3)} errores.")

print("------------------------------------------------------")

'''
24.Desarrollar funciones en Python que resuelvan lo siguiente:
a. Dado un carácter, devolver un byte que represente su código ASCII (7 bits) y utilice
el bit menos significativo para almacenar la paridad del código.
b. Dado un byte que se obtuvo como resultado de la función anterior, verificar si es
correcto o tiene errores
'''
def charToAsciiWithParity(char: str) -> int:
    ascii_value = ord(char)  # Obtener el valor ASCII del carácter
    parity_bit = bin(ascii_value).count('1') % 2  # Calcular el bit de paridad (paridad par)
    ascii_with_parity = (ascii_value << 1) | parity_bit  # Desplazar y agregar el bit de paridad
    return ascii_with_parity

def checkAsciiWithParity(byte: int) -> bool:
    ascii_value = byte >> 1  # Obtener el valor ASCII desplazando a la derecha
    parity_bit = byte & 1  # Obtener el bit de paridad
    # Verificar si la paridad es correcta
    return (bin(ascii_value).count('1') % 2) == parity_bit

print("Ejercicio 26")
'''
26. Codificar funciones en Python que resuelvan lo siguiente:
a. Dada una cadena de caracteres, generar una secuencia de bytes (bytearray) que
contenga su representación con código ASCII y sus bits de paridad vertical,
longitudinal y cruzada.
b. Dada una secuencia de bytes que se obtuvo como resultado de la función anterior,
devolver el mensaje original o una cadena de caracteres vacía si no se pueden
corregir los errores.
Sugerencia: generar una matriz de bits para realizar las operaciones, transformando la
secuencia de bytes en una lista de cadenas de caracteres binarias y, luego, cada cadena
de caracteres en una lista de números enteros que representen los bits.
'''
def stringToByteArrayWithParity(s: str) -> bytearray:
    byte_array = bytearray()
    for char in s:
        byte_array.append(charToAsciiWithParity(char))
        
    # Ahora tengo ue agregar los bits de paridad longitudinal y cruzada
    longitud = len(byte_array)
    parityBitsLongitudinal = []
    for i in range(8):  # Para cada bit de los 8 bits (7 bits ASCII + 1 bit de paridad)
        count = 0
        for j in range(longitud):
            if (byte_array[j] >> (7-i)) & 1:
                count += 1
        parity_bit = count % 2
        parityBitsLongitudinal.append(parity_bit)  # Agregar bit de paridad longitudinal
        
    # 1. Combinar los 8 bits de paridad en un solo byte
    parity_byte = 0
    for bit in parityBitsLongitudinal:
        parity_byte = (parity_byte << 1) | bit
        
    # 2. Insertar ese único byte al principio del array
    byte_array.insert(0, parity_byte)

    return byte_array

def byteArrayToStringWithParity(byte_array: bytearray) -> str:
    original_message = ""
    localByteArray = byte_array[1:]  # Excluir el byte de paridad longitudinal
    longitudinalParityByte = byte_array[0]
    errors = 0
    # Verificar la paridad longitudinal
    for i in range(8):
        count = 0
        for byte in localByteArray:
            if (byte >> (7 - i)) & 1:
                count += 1
        parity_bit = count % 2
        if parity_bit != ((longitudinalParityByte >> (7 - i)) & 1):
            errors += 1
            if errors > 1:
                return ""  # Más de un error, no se puede corregir
    for byte in localByteArray:
        if checkAsciiWithParity(byte):
            original_message += chr(byte >> 1)
        else:
            return ""  # Si hay un error de paridad, devolver cadena vacía
    return original_message

msg = "Hola"
byteArrayWithParity = stringToByteArrayWithParity(msg)
print(f"Byte array con paridad: {byteArrayWithParity}")
decodedMsg = byteArrayToStringWithParity(byteArrayWithParity)
print(f"Mensaje decodificado: {decodedMsg}")