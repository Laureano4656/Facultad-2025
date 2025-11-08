import math
import random


#Mostrar una matriz
def mostrarMatriz(matriz : list[list[float]], titulo : str): 
    print(titulo)
    for fila in matriz:
        print(fila)

#Informacion de cada simbolo calculada a partir de la probabilidad de que este salga
def getInformacion(probabilidades): 
    info = list()
    for prob in probabilidades:
        if prob>0:
            info.append(math.log2(1/prob))
        else:
            info.append(0)
    return info


#Entropia de la fuente calculada a partir de las probabilidades de sus simbolos. El valor medio de la información por símbolo suministrada por la fuente
def getEntropia(probabilidades): 
    info = getInformacion(probabilidades)
    H = 0
    for I,P in zip(info,probabilidades):
        H += I*P
    return H

##
# Que pasa si se quiere calcular la entropia de una fuente con solo un simbolo?
# En este caso, la entropia seria 0, ya que no hay incertidumbre sobre el simbolo que se va a emitir.
# 
# Cual es la maxima entropia posible de una fuente con n simbolos?
# La maxima entropia posible de una fuente con n simbolos es log2(n), que ocurre cuando todos los simbolos tienen la misma probabilidad de ocurrencia (1/n).
# Esto debido a que todos los simbolos son igualmente probables, lo que maximiza la incertidumbre.
##

 #Genero el alfabeto y las probabilidades de sus simbolos dada una cadena
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


#Genero un mensaje dado un alfabeto y las probabilidades de sus simbolos. Longitud N
def generarMensajeAlfabeto(alfabeto, probabilidades,n): 
    s = ""
    for i in range(n):
        j=0
        prob_acum = probabilidades[j]
        r = random.random()
        while (r>prob_acum and j<len(probabilidades)):
            j+=1
            prob_acum+=probabilidades[j]
        if (j<len(probabilidades)):
            s+=alfabeto[j]
        else:
            s+=alfabeto[j-1] #En caso de que la suma de probabilidades no sea 1 y r justo sea 1.
    return s


#Calculo entropia de un alfabeto binario a partir de una probabilidad w
def getEntropiaBinariaW(w): 
    H = getEntropia([w,1-w])
    return H

#Calculo extensiones de grado N a partir de la fuente y de las probabilidades
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
    
def max_vector(vector):
    return max(vector)

def diferencia(v1,v2):
    return [abs(v1[i]-v2[i]) for i in range(len(v1))]

#Calculo el vector estacionario (Aproximacion) a partir de la matriz
def getVecEstacionarioMat(matriz,n): 
    v0 = [1/n]*n
    v1 = [0]*n
    nuevo_v0 = [0]*n
    limite = 0.00001
    while (limite<max_vector(diferencia(v0,v1))):
        v1=v0
        for i in range(n):
            aux=0
            for j in range(n):
                aux+=matriz[i][j]*v0[j]
            nuevo_v0[i]=aux
        v0=nuevo_v0
    return v0

##
# La distribucion de probabilidad de los simbolos en la fuente en el vector t va variando con la evolucion del proceso de emision de simbolos. 
# El vector estacionario representa la distribucion de probabilidad a largo plazo, es decir, la distribucion a la que tiende el sistema despues de muchas transiciones.
# El vector estacionario cumple que V*.M = V*, donde M es la matriz de transicion de estados.
# Esto significa que si el sistema alcanza el vector estacionario, permanecerá en ese estado de distribucion de probabilidad en futuras transiciones.
# En resumen, el vector estacionario es una caracteristica fundamental de las cadenas de Markov y es crucial para entender el comportamiento a largo plazo de la fuente con memoria.
##

#Calculo la entropia a partir de una matriz y su vector estacionario
def getEntropiaConMatVector(matriz,vector_est,n): 
   H=0
   for i in range(n):
       for j in range(n):
           if (matriz[i][j]>0):
                H += vector_est[i]*matriz[j][i]*(-math.log2(matriz[j][i]))
   return H

#Genero la matriz a partir de una cadena dada.
def getMatrizconCad(cadena): 
    alfabeto = []
    n=0
    for i in cadena:
        if i not in alfabeto:
            n+=1
            alfabeto.append(i)
    alfabeto.sort()
    matriz = [[0 for _ in range(n)] for _ in range(n)]
    for idx in range(1, len(cadena)):
        ant = cadena[idx-1]
        k = cadena[idx]
        if ant in alfabeto and k in alfabeto:
            i = alfabeto.index(ant)
            j = alfabeto.index(k)
            matriz[i][j] += 1
    for j in range(n):
        total = sum(matriz[i][j] for i in range(n))
        if total > 0:
            for i in range(n):
                matriz[i][j] /= total
    return alfabeto,matriz

def calcTransitions(msg, alphabet, i, j):
    # Inicializamos el contador de transiciones
    transitions = 0

    # Recorremos el mensaje, excepto el último índice
    for k in range(len(msg) - 1):
        # Si el carácter actual es alphabet[i] y el siguiente es alphabet[j]
        if msg[k] == alphabet[i] and msg[k + 1] == alphabet[j]:
            transitions += 1  # Incrementamos el contador

    return transitions

def getMatriz(alphabet,msg):
  n = len(alphabet)
  cantAlph = []
  for alph in alphabet:
    cantAlph.append(msg.count(alph))
  M = [[0] * n for _ in range(n)]
  cantAlph[alphabet.index(msg[len(msg)-1])] -=1
  for j in range(n):
    for i in range(n):
      M[i][j] = calcTransitions(msg,alphabet,i,j) / cantAlph[i]
  return M
##
# Si la cadena dada es lo suficientemente larga, la matriz de transicion de estados generada a partir de ella sera una buena aproximacion de la matriz real de la fuente.
# Si la cadena es corta, la matriz generada puede no reflejar con precision las probabilidades de transicion entre estados.
# Ademas, si la cadena no contiene todas las posibles transiciones entre simbolos del alfabeto, algunas entradas de la matriz seran cero, lo que puede afectar el calculo del vector estacionario y la entropia.
##      


##Genero una cadena a partir de su matriz de markov y alfabeto
def getCadenaConMatriz(matriz,alfabeto,n): 
    cadena = random.choice(alfabeto)
    for i in range(n):
        ultimo=cadena[-1]
        prob=random.random()
        idx = alfabeto.index(ultimo)
        acum=0
        j=0
        acum+=matriz[j][idx]
        while (j<len(matriz) and prob>=acum):
            j+=1
            acum+=matriz[j][idx]
        cadena+=alfabeto[j]
    return cadena

##
# Si la matriz de transicion de estados es correcta y el alfabeto es completo, la cadena generada sera una buena representacion del comportamiento de la fuente.
# La probabilidad de cada simbolo en la cadena dependera de las probabilidades de transicion definidas en la matriz.
# Si la matriz es incorrecta o incompleta, la cadena generada puede no reflejar con precision las propiedades de la fuente.
##


#Busca la maxima diferencia entre probabilidades de los simbolos, si esta es mayor a la tolerancia la fuente tiene memoria, sino tiene memoria nula
def isMemoriaNula(matriz,tolerancia): 
    maxima_dif = []
    for i in range(len(matriz)):
        maxima_dif.append(max(matriz[i])-min(matriz[i]))
    maxima = max(maxima_dif)
    if maxima<tolerancia:
        return True
    else:
        return False
            
##########################################################
                    #GUIA3#
##########################################################


# Un codigo es no singular si todas sus palabras codigo son distintas. Va a ser decodificable pero puede ser ambiguo
def isNoSingular(codigo):
  i = 0
  while (i<len(codigo) and codigo.count(codigo[i])==1):
    i+=1
  return i==len(codigo)

# Un codigo es instantaneo si ninguna palabra codigo es prefijo de otra palabra codigo. Puede decodificarse a medida que se recibe cada simbolo
def isInstantaneo(codigo):
  band = True
  i = 0
  while (i<len(codigo) and band):
    j=0
    while (j<len(codigo) and band):
      if (j!=i and codigo[j].startswith(codigo[i])):
        band = False
      j+=1
    i+=1
  return band

# Un codigo es univocamente decodificable si cualquier secuencia de simbolos del alfabeto puede ser decodificada de una unica manera
def isUnivoco(codigo): # Algoritmo de Sardinas-Patterson
  S = [set(codigo), set()] # Lista de conjuntos ya vistos
  i = 0 # Numero de Iteraciones
  seguir = True
  while seguir:
      print(S[i])
      for x in S[0]: # Siempre comparo con el codigo
          for y in S[i]: # En S[i] se guarda el conjunto el cual debo comparar con S[0]
              if x.startswith(y) and x != y:
                  S[i+1].add(x[len(y):])
              else:
                  if y.startswith(x) and x != y:
                      S[i+1].add(y[len(x):])
      if S[0].intersection(S[i+1]) != set(): # Si la intersección no es vacía, no es unívocamente decodificable
          respuesta = False
          seguir = False
      else:
          if S[i+1] == set() or S[i+1] in S[0:i+1]: # Si en la pasada me quedo un conjunto vacio o el conjunto que me quedo ya lo vi antes entonces es un codigo univocamente decodificable
              respuesta = True
              seguir = False
          else:
              S.append(set()) # Si no encontre nada sigo buscando
              i += 1
  return respuesta


def getTipoCodigo(codigo):
    if (not isNoSingular(codigo)): #Si no es no singular => es bloque o singular
        return ("El codigo es de tipo bloque o singular")
    else:
        if (isInstantaneo(codigo)):
            return ("El codigo es instantaneo")  
        else:
            if (isUnivoco(codigo)):
                return ("El codigo es univoco")
            else:
                return ("El codigo es no singular")
            
##
# Codigo Bloque o singular, NO SON DECODIFICABLES
# Codigo No Singular, SI SON decodificables pero ambiguos, es decir, una misma cadena puede tener mas de una decodificacion posible
# Codigo Univoco, SI SON DECODIFICABLES pero no se pueden decodificar a medida que se reciben los simbolos, hay que obtener la cadena completa
# Codigo Instantaneo, SI SON DECODIFICABLES y ademas se pueden decodificar a medida que se reciben los simbolos
##


 # Dada una lista de palabras codigo devuelve el alfabeto codigo
def getAlfabetoCodigo(codigo): 
    alfabeto = set()
    for elemento in codigo:
        for caracter in elemento:
            alfabeto.add(caracter)
    return alfabeto


# Devuelve una lista con las longitudes de cada palabra codigo
def getLongitudesPalabrasCod(codigo): 
    longitud = list()
    for palabra in codigo:
        longitud.append(len(palabra))
    return longitud


# Devuelve el valor de realizar la Sumatoria de la Inecuacion de Kraft
def getKraft(alfabeto,longitud): 
    sumatoria = 0
    for i in range(len(longitud)):
        sumatoria += len(alfabeto)**(-longitud[i])
    return sumatoria # Si esta es <= 1 entonces existe un codigo Instantaneo con estas longitudes

##
# Si el codigo es univoco, entonces la suma de la inecuacion de Kraft sera menor o igual a 1.
# Si la suma es mayor a 1, entonces el codigo no sera univocamente decodificable, por ende tampoco sera instantaneo.
# Me asegura la existencia de una combinacion de palabras codigo de las mismas longitudes que las palabras codigo dadas para que el codigo sea instantaneo.
##


 # Calcula la entropia del codigo, con el logaritmo en base r (Longitud del Alfabeto codigo)
def getEntropiaCodigoR(codigo, probabilidad):
    s = 0
    alfabeto = getAlfabetoCodigo(codigo)
    r = len(alfabeto)
    for prob in probabilidad:
        s+=prob*math.log(1/prob,r)
    return s

# Calculo la longitud media del codigo
def getLongitudMedia(palabras_codigo, probabilidad): 
    l = 0
    for i in range(len(palabras_codigo)):
        l += probabilidad[i]*len(palabras_codigo[i])
    return l


# Dadas las palabras codigo y sus probabilidades se determina si este es compacto mediante 
# el uso de que la Longitud de la palabra codigo sea menor igual a su Informacion otorgada
def isCompacto(palabras_codigo, probabilidad): 
    alfabeto = getAlfabetoCodigo(palabras_codigo)
    r = len(alfabeto)
    bandera = False
    if (isInstantaneo(palabras_codigo)):
        bandera=True
        for elemento,prob in zip(palabras_codigo,probabilidad):
            if(not(len(elemento)<=math.ceil(math.log(1/prob,r)))):
                bandera = False
                break
    return bandera


# Genera un mensaje codificado a partir de las palabras codigo
def generarMensajeCodigo(palabras_codigo, probabilidades, n): 
    s = ""
    for i in range(n):
        j = 0
        acum = probabilidades[j]
        letra = random.random()
        while (acum<letra):
            j+=1
            acum += probabilidades[j]
        s += palabras_codigo[j]
    return s


def probabilidadesOrdenN(probs, N):
    if N == 1:
        return probs
    else:
        probsN = []
        for p in probabilidadesOrdenN(probs, N-1):
            for prob in probs:
                probsN.append(p * prob)
        return probsN



###########################################################
                    #TP4#
###########################################################

def verificar_primer_teorema(probabilidades, codigo, N):
    # Calcular la entropía de la fuente
    H = getEntropiaCodigoR(codigo,probabilidades)
    
    # Calcular la longitud promedio del código

    probsExtension = probabilidadesOrdenN(probabilidades, N)
    Ln = getLongitudMedia(codigo, probsExtension)

    # Verificar el Primer Teorema de Shannon
    cumple_teorema = H <= Ln / N <= H + (1/N)
    
    return cumple_teorema


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

## Solucion valen:
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

# solucion enzo:

def generarCodigoShannonFano(probabilidades):
    lista = [[p, i] for i, p in enumerate(probabilidades)];
    lista = sorted(lista, key=lambda x: x[0], reverse=True);
    codigo = [""] * len(probabilidades);
    n = len(probabilidades);
    def shanonFano(lista):
        if len(lista) == 1:
            return;
        suma = sum([x[0] for x in lista]);
        suma_parcial = 0;
        i = 0;
        while suma_parcial + lista[i][0] < suma / 2:
            suma_parcial += lista[i][0];
            i += 1;
        for j in range(i + 1):
            codigo[lista[j][1]] += "1";
        for j in range(i + 1, len(lista)):
            codigo[lista[j][1]] += "0";
        shanonFano(lista[:i + 1]);
        shanonFano(lista[i + 1:]);
    shanonFano(lista);
    return codigo;


def calcularRendimiento(probabilidades, codigo):
    H = getEntropiaCodigoR(codigo,probabilidades)
    L = getLongitudMedia(codigo,probabilidades)
    R = H / L if L != 0 else 0
    D = 1 - R
    return R

def calcularRedundancia(probabilidades, codigo):
    H = getEntropiaCodigoR(codigo,probabilidades)
    L = getLongitudMedia(codigo,probabilidades)
    R = H / L if L != 0 else 0
    D = 1 - R
    return D

def codeMessage(codigo: list, mensaje: str,alfabeto = [],) -> bytearray:
    if not len(alfabeto) :
        alfabeto, _ = getAlfabetoyProbabilidades(mensaje)
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

def calcularTasaCompresion(mensaje: str, mensajeCodificado: bytearray) -> float:
    tamanio_original = len(mensaje) * 8; # Tamaño en bits del mensaje original
    tamanio_codificado = len(mensajeCodificado) * 8; # Tamaño en bits del mensaje codificado
    return tamanio_original / tamanio_codificado;

def createFile(name: str, byte_array: bytearray):
    with open(name, 'wb') as file:
        file.write(byte_array)

def readFile(name: str) -> bytearray:
    with open(name, 'rb') as file:
        byte_array = bytearray(file.read())
    return byte_array

def compressRLCToBytes(mensaje: str) -> bytearray:
    """
        Comprime un mensaje usando Run Length Encoding (RLC).
        Devuelve un byteArray con el mensaje comprimido
    """
    mensaje_comprimido = bytearray();
    n = len(mensaje) - 1;
    i = 0;
    while i < n:
        simbolo = mensaje[i];
        contador = 1;
        while i < n and mensaje[i] == mensaje[i + 1]:
            contador += 1;
            i += 1;
        i += 1;
        mensaje_comprimido.append(ord(simbolo)); # Convierto el simbolo a su valor ASCII
        mensaje_comprimido.append(contador);
    if mensaje[n] != mensaje[n - 1]: # Si el ultimo simbolo es distinto al penultimo
        mensaje_comprimido.append(ord(mensaje[n]));
        mensaje_comprimido.append(1);
    return mensaje_comprimido;

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

def agregarBitParidadPalabra(palabra: str) -> str:
    count = palabra.count('1')
    if count % 2 == 0:
        return palabra + '0'  # Agrego un 0 si la cantidad de 1s es par
    else:
        return palabra + '1'  # Agrego un 1 si la cantidad de 1s es impar

def charToAsciiWithParity(char: str) -> int:
    ascii_value = format(ord(char), '07b')  # Obtener el valor ASCII del carácter en 7 bits
    ascii_with_parity = agregarBitParidadPalabra(ascii_value)  # Agregar bit de paridad
    return int(ascii_with_parity, 2)  # Convertir de binario a entero

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

def convertMatrixToByteArray(matriz: list[list[float]]) -> bytearray:
    byte_array = bytearray()
    for fila in matriz:
        codigo_ascii = ''.join([str(bit) for bit in fila])  # Convierto la lista de enteros a un string
        byte_array.append(int(codigo_ascii, 2))  # Convierto el codigo ASCII a un caracter
    return byte_array

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

    # Verificar la paridad VRC
    for i in range(1, len(matriz)):  # Empiezo desde 1 para saltar la fila de paridad VRC
        fila = matriz[i][:-1]  # Saco la última columna que es la de paridad
        cantidad_1s = sum(fila)
        parity_bit = cantidad_1s % 2        
        if parity_bit != matriz[i][-1]:  # Si la paridad no es correcta
            if posiciones_error.count((i, i)) <= 0:  # Si no se detectó un error longitudinal en esta fila
                errors += 1
                print(f"Error en paridad VRC en fila {i}")
                if errors > 1:
                    return ""  # No se puede corregir el error
                posiciones_error.append((i, i))  # 'V' para VRC
        else:
            # Si la paridad es correcta, decodifico el caracter
            codigo_ascii = ''.join([str(bit) for bit in fila])  # Convierto la lista de enteros a un string
            caracter = chr(int(codigo_ascii, 2))  # Convierto el codigo ASCII a un caracter
            original_message += caracter
    
    # Corregir errores si es posible
    if errors == 1:
        error_pos = posiciones_error[0]
        fila_error = error_pos[0]
        columna_error = error_pos[1]
        matriz[fila_error][columna_error] ^= 1  # Corregir el bit erróneo
        print(f"Corrigiendo error en fila {fila_error}, columna {columna_error}")
        # Decodifico el mensaje corregido
        original_message = ""
        for i in range(1, len(matriz)):  # Empiezo desde 1 para saltar la fila de paridad VRC
            fila = matriz[i][:-1]  # Saco la última columna que es la de paridad
            codigo_ascii = ''.join([str(bit) for bit in fila])  # Convierto la lista de enteros a un string            
            caracter = chr(int(codigo_ascii, 2))  # Convierto el codigo ASCII a un caracter
            original_message += caracter

    return original_message


#######################################################
#                  #TP5#
#######################################################

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
        total_apariciones = conteo_entrada[simbolo_in]
        if total_apariciones > 0:
            for j in range(numColumnas):
                matrizCanal[i][j] = conteo_pares[i][j] / total_apariciones
    
    return matrizCanal

def getProbabilidadesSalida(probsPriori: list[float], matrizCanal: list[list[float]]) -> list[float]:
    
    num_simbolos_salida = len(matrizCanal[0])
    probs_salida = [0.0] * num_simbolos_salida

    for j in range(num_simbolos_salida):
        for i in range(len(probsPriori)):
            probs_salida[j] += probsPriori[i] * matrizCanal[i][j]

    return probs_salida

def getProbabilidadesSalidaConMsg(entrada: str, salida: str) -> list:
    matrizCanal = getMatrizCanal(entrada, salida)
    probsPriori =getAlfabetoyProbabilidades(entrada)[1]
    num_simbolos_salida = len(matrizCanal[0])
    probs_salida = [0.0] * num_simbolos_salida

    for j in range(num_simbolos_salida):
        for i in range(len(probsPriori)):
            probs_salida[j] += probsPriori[i] * matrizCanal[i][j]

    return probs_salida

def getProbabilidadesSimultaneasConMsg(entrada: str, salida: str) -> list:
    matrizCanal = getMatrizCanal(entrada, salida)
    probsPriori =getAlfabetoyProbabilidades(entrada)[1]
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
    probsSimultaneas = getProbabilidadesSimultaneas(probsPriori, matrizCanal)
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

def verificarRelaciones(probsPriori: list[float], matrizCanal: list[list[float]]) -> bool:
    entropiaPriori = getEntropia(probsPriori)
    probsSalida = getProbabilidadesSalida(probsPriori, matrizCanal)
    entropiaSalida = getEntropia(probsSalida)
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


#############################################
#               TP6
#############################################
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

def getCanalCompuesto(canalA: list[list[float]], canalB: list[list[float]]) -> list[list[float]]:
    """
    Obtiene la matriz del canal compuesto de dos canales.
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
