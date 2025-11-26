import math
""""
Dado el siguiente mensaje, emitido por una fuente de información:

Obtener las probabilidades de los símbolos y la entropía de la fuente
Generar un código binario óptimo para la fuente de información
Determinar la tasa de compresión que se obtiene codificando el mensaje
Generar un código binario óptimo para la extensión de orden 3
Calcular la longitud media, el rendimiento y la redundancia de cada código
Verificar si ambos códigos cumplen con el Primer Teorema de Shannon
Aclaración: no incluir ningún tipo de redundancia adicional en la codificación, debe contener únicamente los códigos de los símbolos del mensaje.

Mensaje = GIIHGGGHGIHHIHIIGFHH
"""
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
def codeMessage(codigo: list, mensaje: str,alfabeto: list[float] = []) -> bytearray:

    """Codifica un mensaje usando un código binario dado y devuelve un bytearray.
    Args:
        codigo (list): Lista de códigos binarios para cada símbolo.
        mensaje (str): Mensaje a codificar.
        alfabeto (list[float], optional): Alfabeto de símbolos. Defaults to [].

    Returns:
        bytearray: Bytearray que contiene el mensaje codificado.
    """
    if not len(alfabeto) :
        alfabeto, _ = getAlfabetoyProbabilidades(mensaje)
    # Crear un diccionario para mapear cada símbolo a su código binario
    codigoDict = {alfabeto[i]: codigo[i] for i in range(len(alfabeto))}
    
    # Codificar el mensaje
    mensajeCodificado = ''.join(codigoDict[char] for char in mensaje)
    longitudMsgCodificado = len(mensajeCodificado)
        
    # bitsRelleno = 0
    # while longitudMsgCodificado % 8 != 0:
    #     mensajeCodificado += '0'  # Rellenar con ceros a la derecha
    #     bitsRelleno += 1
    #     longitudMsgCodificado += 1

    # Convertir la cadena de bits en un bytearray
    byte_array = bytearray()
    #byte_array.append(bitsRelleno)  # Primer byte indica la cantidad de bits de relleno
    for i in range(0, len(mensajeCodificado), 8):
        byte_segment = mensajeCodificado[i:i+8]
        byte_array.append(int(byte_segment, 2))  # Rellenar con ceros a la derecha si es necesario
    
    return byte_array

def calcularTasaCompresion(mensaje: str, mensajeCodificado: bytearray) -> float:
    tamanio_original = len(mensaje) * 8; # Tamaño en bits del mensaje original
    tamanio_codificado = len(mensajeCodificado) * 8; # Tamaño en bits del mensaje codificado
    return tamanio_original / tamanio_codificado;

def calcExtensionN(fuente,probabilidades,n): 
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

def getLongitudesPalabrasCod(codigo): 
    return [len(cod) for cod in codigo];
def getLongitudMedia(palabras_codigo, probabilidad): 
    return sum([p * l for p, l in zip(probabilidad, getLongitudesPalabrasCod(palabras_codigo))]);

def getAlfabetoCodigo(codigo): 
    alfabeto = set()
    for elemento in codigo:
        for caracter in elemento:
            alfabeto.add(caracter)
    return alfabeto

def getEntropiaCodigoR(codigo, probabilidad):
    s = 0
    alfabeto = getAlfabetoCodigo(codigo)
    r = len(alfabeto)
    for prob in probabilidad:
        s+=prob*math.log(1/prob,r)
    return s

def calcularRendimiento(probabilidades, codigo):
    H = getEntropiaCodigoR(codigo,probabilidades)
    L = getLongitudMedia(codigo,probabilidades)
    R = H / L if L != 0 else 0    
    return R

def calcularRedundancia(probabilidades, codigo):
    H = getEntropiaCodigoR(codigo,probabilidades)
    L = getLongitudMedia(codigo,probabilidades)
    R = H / L if L != 0 else 0
    D = 1 - R
    return D

def probabilidadesOrdenN(probs, N):
    if N == 1:
        return probs
    else:
        probsN = []
        for p in probabilidadesOrdenN(probs, N-1):
            for prob in probs:
                probsN.append(p * prob)
        return probsN
def verificar_primer_teorema(probabilidades, codigo, N):
    # Calcular la entropía de la fuente
    H = getEntropiaCodigoR(codigo,probabilidades)
    
    # Calcular la longitud promedio del código

    probsExtension = probabilidadesOrdenN(probabilidades, N)
    Ln = getLongitudMedia(codigo, probsExtension)

    # Verificar el Primer Teorema de Shannon
    cumple_teorema = H <= Ln / N <= H + (1/N)
    
    return cumple_teorema


mensaje = "GIIHGGGHGIHHIHIIGFHH"

fuente,probsSimbolos = getAlfabetoyProbabilidades(mensaje)
entropia = getEntropia(probsSimbolos)
codigoOptimo = getCodigoHuffman(probsSimbolos)

codificado = codeMessage(codigoOptimo, mensaje,fuente)

tasaCompresion = calcularTasaCompresion(mensaje, codificado)

fuente3,extension3 = calcExtensionN(fuente,probsSimbolos, 3)

codigoOptimoExt3 = getCodigoHuffman(extension3)

longitudMedia1 = getLongitudMedia(codigoOptimo, probsSimbolos)
rendimiento1 = calcularRendimiento(probsSimbolos,codigoOptimo)
redundancia1 = calcularRedundancia(probsSimbolos,codigoOptimo)

longitudMedia2 = getLongitudMedia(codigoOptimoExt3, extension3)
rendimiento2 = calcularRendimiento(extension3,codigoOptimoExt3)
redundancia2 = calcularRedundancia(extension3,codigoOptimoExt3)

shannon1 = verificar_primer_teorema(probsSimbolos, codigoOptimo,1)
shannon2 = verificar_primer_teorema(extension3,codigoOptimoExt3,1)

print("Resultados: ")

print("Entropia de la fuente: ",entropia)
print("Probabilidades de los simbolos: ",probsSimbolos)
print("Tasa de compresion ",tasaCompresion,":1")
print("mensaje codificado: ",codificado)

print("\nCodigo Optimo para la fuente: ", codigoOptimo)
print("Longitud media del codigo optimo: ",longitudMedia1)

print("Rendimiento del codigo optimo: ",rendimiento1)
print("Redundancia del codigo optimo: ",redundancia1)

print("Cumple con el primer teorema de Shannon: ",shannon1)

print("\nCodigo Optimo para la extension de orden 3: ", codigoOptimoExt3)
print("Longitud media del codigo optimo de la extension de orden 3: ",longitudMedia2)
print("Rendimiento del codigo optimo de la extension de orden 3: ",rendimiento2)
print("Redundancia del codigo optimo de la extension de orden 3: ",redundancia2)
print("Cumple con el primer teorema de Shannon: ",shannon2)