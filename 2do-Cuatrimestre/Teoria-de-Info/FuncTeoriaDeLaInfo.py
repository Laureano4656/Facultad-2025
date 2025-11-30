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

def getVecEstacionarioMat(matriz): 
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

##
# La distribucion de probabilidad de los simbolos en la fuente en el vector t va variando con la evolucion del proceso de emision de simbolos. 
# El vector estacionario representa la distribucion de probabilidad a largo plazo, es decir, la distribucion a la que tiende el sistema despues de muchas transiciones.
# El vector estacionario cumple que V*.M = V*, donde M es la matriz de transicion de estados.
# Esto significa que si el sistema alcanza el vector estacionario, permanecerá en ese estado de distribucion de probabilidad en futuras transiciones.
# En resumen, el vector estacionario es una caracteristica fundamental de las cadenas de Markov y es crucial para entender el comportamiento a largo plazo de la fuente con memoria.
##

#Calculo la entropia a partir de una matriz y su vector estacionario
def calcularEntropiaFuenteMarkov(mat, vec_est):
    entropia = 0;
    for j in range(len(mat)):
        sum = 0;
        for i in range(len(mat)):
            if mat[i][j] != 0:
                sum += mat[i][j] * math.log2(1/mat[i][j]); # Esta en base 2
        entropia += vec_est[j] * sum;
    return entropia;

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
  print(i)
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
      #print(S[i])
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
    return [len(cod) for cod in codigo];


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
    return sum([p * l for p, l in zip(probabilidad, getLongitudesPalabrasCod(palabras_codigo))]);


# Dadas las palabras codigo y sus probabilidades se determina si este es compacto mediante 
# el uso de que la Longitud de la palabra codigo sea menor igual a su Informacion otorgada
def isCompacto(palabras_codigo, probabilidad): 
    if not isInstantaneo(palabras_codigo):
        return False;
    r = len(getAlfabetoCodigo(palabras_codigo));
    longitudes = getLongitudesPalabrasCod(palabras_codigo);
    for i in range(len(palabras_codigo)):
        if longitudes[i] > math.ceil(math.log(1/probabilidad[i], r)):
            return False;
    return True;


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
"""
Primer teorma de shannon. Determina si se verifica el primer teorema de shannon
dado un conjunto de probabilidades, un codigo y un orden N.
Para realizar esto obtiene la entropia del codigo, las probabilidades de la extension (orden N) de la fuente
y la longitud media del codigo para dichas probabilidades.
"""
def verificar_primer_teorema(probabilidades, codigo, N):
    # Calcular la entropía de la fuente
    H = getEntropiaCodigoR(codigo,probabilidades)
    
    # Calcular la longitud promedio del código

    probsExtension = probabilidadesOrdenN(probabilidades, N)
    Ln = getLongitudMedia(codigo, probsExtension)

    # Verificar el Primer Teorema de Shannon
    cumple_teorema = H <= Ln / N <= H + (1/N)
    
    return cumple_teorema

"""
Pasos algoritmo de Huffman:
 Consideremos S: {s1, s2,..,sq} y P {p1,P2 , ..., Pq }
    1. INICIALIZACIÓN: Cada símbolo se asocia con su probabilidad.
    2. BUCLE ITERATIVO: Mientras haya más de un símbolo en la lista:
        a. Ordenar la lista de símbolos por probabilidad.
        b. Extraer los dos símbolos con las menores probabilidades.
        c. CONSTRUCCIÓN DE CÓDIGOS: A los símbolos del primer grupo se les añade un '0' al inicio de su código, y a los del segundo grupo un '1'.
        d. COMBINACIÓN: Crear un nuevo símbolo que combine ambos grupos, con una probabilidad igual a la suma de las dos.
    3. RESULTADO: Al finalizar, cada símbolo tendrá un código binario único asignado.

"""
"""
=============================================================================
PRUEBA DE ESCRITORIO: getCodigoHuffman
=============================================================================
DATOS DE ENTRADA (probs): [0.5, 0.25, 0.15, 0.10]
ÍNDICES ORIGINALES:        0     1     2     3

1. INICIALIZACIÓN
   --------------------------------------------------------------------------
   items:   [[0.5, [0]], [0.25, [1]], [0.15, [2]], [0.10, [3]]]
   codigos: ["", "", "", ""]

2. BUCLE ITERATIVO
   --------------------------------------------------------------------------
   >> VUELTA 1 (len > 1)
      Sort:    [[0.10, [3]], [0.15, [2]], [0.25, [1]], [0.5, [0]]]
      Pop:     Menor = [0.10, [3]] (idx 3)
               Mayor = [0.15, [2]] (idx 2)
      Update:  codigos[3] prepende "0" -> "0"
               codigos[2] prepende "1" -> "1"
      Push:    [0.25, [3, 2]] (Suma de prob: 0.10 + 0.15)

   >> VUELTA 2 (len > 1)
      Sort:    [[0.25, [1]], [0.25, [3, 2]], [0.5, [0]]]
      Pop:     Menor = [0.25, [1]]    (idx 1)
               Mayor = [0.25, [3, 2]] (idxs 3 y 2)
      Update:  codigos[1] prepende "0"   -> "0"
               codigos[3] prepende "1"   -> "1" + "0" = "10"
               codigos[2] prepende "1"   -> "1" + "1" = "11"
      Push:    [0.5, [1, 3, 2]] (Suma: 0.25 + 0.25)

   >> VUELTA 3 (len > 1)
      Sort:    [[0.5, [0]], [0.5, [1, 3, 2]]]
      Pop:     Menor = [0.5, [0]]       (idx 0)
               Mayor = [0.5, [1, 3, 2]] (idxs 1, 3 y 2)
      Update:  codigos[0] prepende "0"   -> "0"
               codigos[1] prepende "1"   -> "1" + "0"  = "10"
               codigos[3] prepende "1"   -> "1" + "10" = "110"
               codigos[2] prepende "1"   -> "1" + "11" = "111"
      Push:    [1.0, [0, 1, 3, 2]]

3. RESULTADO FINAL (Retorno)
   --------------------------------------------------------------------------
   Índice 0 (0.50): "0"
   Índice 1 (0.25): "10"
   Índice 2 (0.15): "111"
   Índice 3 (0.10): "110"
=============================================================================
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

"""
Toma el techo de la longitud mediia como la entropia del codigo + 2, en lugar de más de 1 como en el teorema de Shannon.
Pasos algoritmo de Shannon-Fano:
    1. ORDENAR: Ordenar los símbolos en orden descendente según sus probabilidades.
    2. DIVIDIR: Dividir la lista en dos grupos, de modo que la suma de las probabilidades de cada grupo sea lo más cercana posible.
    3. ASIGNAR CÓDIGOS: Asignar un '0' a todos los símbolos del primer grupo y un '1' a los del segundo grupo.
    4. RECURSIVIDAD: Aplicar recursivamente el proceso a cada grupo hasta que cada símbolo tenga un código único.
"""
"""
=============================================================================
EJEMPLO DE EJECUCIÓN: getCodigoShannonFano
=============================================================================
DATOS DE ENTRADA (probs): [0.4, 0.3, 0.2, 0.1]
ÍNDICES ORIGINALES:        0    1    2    3

NOTA SOBRE PREFIJOS EN ESTE CÓDIGO:
- Grupo Superior (codigos1) se le asigna prefijo "1".
- Grupo Inferior (codigos2) se le asigna prefijo "0".

-----------------------------------------------------------------------------
NIVEL 0 (Raíz): [0.4, 0.3, 0.2, 0.1] | Total = 1.0
-----------------------------------------------------------------------------
1. ORDENAR (Descendente): Ya están ordenados.
2. BUSCAR PUNTO DE CORTE (Donde |SumaIzq - SumaDer| sea mínima):
   - Corte tras 0.4: Izq(0.4) vs Der(0.6) -> Dif = 0.2  <-- ¡MEJOR CORTE!
   - Corte tras 0.7: Izq(0.7) vs Der(0.3) -> Dif = 0.4

3. DIVISIÓN Y RECURSIÓN:
   > GRUPO 1 (Superior): [0.4]
     - Caso base (len=1): Retorna [""]
     - Asignar bit: Se añade "1". Resultado parcial: ["1"]

   > GRUPO 2 (Inferior): [0.3, 0.2, 0.1] (Llamada Recursiva - Ver Nivel 1)
     - Recibe de la recursión: ["1", "01", "00"]
     - Asignar bit: Se añade "0" a todo.
     - Resultado parcial: ["01", "001", "000"]

-----------------------------------------------------------------------------
NIVEL 1 (Procesando el Grupo Inferior del Nivel 0): [0.3, 0.2, 0.1] | Total = 0.6
-----------------------------------------------------------------------------
1. BUSCAR PUNTO DE CORTE:
   - Corte tras 0.3: Izq(0.3) vs Der(0.3) -> Dif = 0.0 <-- ¡PERFECTO!

2. DIVISIÓN Y RECURSIÓN:
   > SUB-GRUPO A (Superior): [0.3]
     - Caso base: Retorna [""]
     - Asignar bit: Se añade "1". Resultado: ["1"]

   > SUB-GRUPO B (Inferior): [0.2, 0.1] (Llamada Recursiva - Ver Nivel 2)
     - Recibe de la recursión: ["1", "0"]
     - Asignar bit: Se añade "0" a todo.
     - Resultado: ["01", "00"]

-----------------------------------------------------------------------------
NIVEL 2 (Procesando el Sub-Grupo B del Nivel 1): [0.2, 0.1] | Total = 0.3
-----------------------------------------------------------------------------
1. BUSCAR PUNTO DE CORTE:
   - Corte tras 0.2: Izq(0.2) vs Der(0.1) -> Dif = 0.1

2. DIVISIÓN:
   > HOJA SUP (0.2): Retorna [""] -> Añade "1" -> ["1"]
   > HOJA INF (0.1): Retorna [""] -> Añade "0" -> ["0"]

-----------------------------------------------------------------------------
RECONSTRUCCIÓN FINAL (Mapeo a índices originales)
-----------------------------------------------------------------------------
Se combinan los resultados de las llamadas recursivas en el orden original:

Índice 0 (0.4) -> "1"
Índice 1 (0.3) -> "01"
Índice 2 (0.2) -> "001"
Índice 3 (0.1) -> "000"
=============================================================================
"""
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

def longitudes_Huffman_ShannonFano(codificacion):
    for codigo in codificacion:
        print(len(codigo))
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

"""
El rendimiento o eficiencia de un código mide qué tan cerca está la longitud media
del código (L) de la entropía (H) de la fuente. Se calcula como R = H / L.
El R es máximo si L es igual a H, lo que indica que el código es óptimo.
Se calcula obteniendo la entropía del código, la longitud media de sus símbolos
y aplicando la formula R = H / L.
"""
def calcularRendimiento(probabilidades, codigo):
    H = getEntropiaCodigoR(codigo,probabilidades)
    L = getLongitudMedia(codigo,probabilidades)
    R = H / L if L != 0 else 0    
    return R

"""
La redundancia de un código se define como 1-R = (L - H) / L, donde R es el rendimiento del código.
Mayor redundancia implica menor información. Cuando el código es óptimo, la redundancia es mínima.
Se calcula obteniendo la entropía del código, la longitud media de sus símbolos, aplicando la formula del rendimiento
y restando el resultado a 1.
"""
def calcularRedundancia(probabilidades, codigo):
    H = getEntropiaCodigoR(codigo,probabilidades)
    L = getLongitudMedia(codigo,probabilidades)
    R = H / L if L != 0 else 0
    D = 1 - R
    return D

"""
Codifica un mensaje usando un código binario dado y devuelve un bytearray.
El primer byte del bytearray indica la cantidad de bits de relleno añadidos al final
para completar el último byte.
PASOS:
1. Crear un diccionario que mapea cada símbolo del alfabeto a su código binario.
2. Recorrer el mensaje original y construir la cadena de bits codificada.
3. Añadir bits de relleno (ceros) al final para que la longitud total sea múltiplo de 8.
4. Convertir la cadena de bits en un bytearray, donde el primer byte indica la cantidad de bits de relleno.

"""
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

"""
Decodifica un mensaje codificado en un bytearray usando un código binario dado.
PASOS:
1. Crear un diccionario que mapea cada código binario a su símbolo correspondiente.
2. Convertir el bytearray de nuevo a una cadena de bits.
3. Eliminar los bits de relleno al final según lo indicado en el primer byte.
4. Recorrer la cadena de bits y decodificar el mensaje utilizando el diccionario.
"""
def decodeMessage(alfabeto: list, codigo: list, byte_array: bytearray) -> str:
    """
    Decodifica un mensaje codificado en un bytearray usando un código binario dado.

    Args:
        alfabeto (list): Lista de símbolos del alfabeto.
        codigo (list): Lista de códigos binarios para cada símbolo.
        byte_array (bytearray): Bytearray que contiene el mensaje codificado.

    Returns:
        str: Mensaje decodificado.
    """
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

"""
La tasa de compresión mide que tan grande era el mensaje original en comparación con su versión comprimida.
"""
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
"""
    Comprime un mensaje usando Run Length Encoding (RLC).
    Pasos:
    1. Inicializar un bytearray vacío para el mensaje comprimido.
    2. Recorrer el mensaje original y contar las ocurrencias consecutivas de cada símbolo
    3. Para cada símbolo y su contador, agregar al bytearray el valor ASCII del símbolo y el contador.
    4. Devolver el bytearray con el mensaje comprimido.
"""
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

"""
Se define como Distancia de Hamming entre dos palabras al número de bits que difieren una
de otra. La distancia de Hamming mínima de un código es la menor distancia de Hamming
entre todas las parejas de palabras código del mismo.
PASOS:
1. Inicializar una variable para la distancia mínima con un valor alto.
2. Recorrer todas las parejas de palabras código y calcular la distancia de Hamming entre ellas.
3. Si la distancia calculada es menor que la distancia mínima actual, actualizar la distancia mínima
"""
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

"""
Convierte una cadena de caracteres en un bytearray, agregando bits de paridad VRC y LRC.
Se utilizar el criterio de paridad par: 0 si la cantidad de 1s es par, 1 si es impar.
PASOS:
1. Convertir cada carácter a su valor ASCII de 7 bits y agregar un bit de paridad VRC.
2. Calcular los bits de paridad longitudinal (LRC) para cada bit de las posiciones 0 a 7.
3. Combinar los bits de paridad LRC en un solo byte y agregarlo al principio del bytearray.
4. Devolver el bytearray resultante.
"""
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
"""
Convierte un bytearray con bits de paridad VRC y LRC de vuelta a la cadena original,
corrigiendo errores si es posible.
PASOS:
1. Convertir el bytearray a una matriz de bits.
2. Verificar la paridad cruzada, longitudinal y VRC.
3. Si se detecta un error, intentar corregirlo si es posible.
4. Decodificar los caracteres originales de la matriz y devolver la cadena resultante.
"""
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
        if parity_bit != matriz[i][-1]:  # Si la paridad no es correcta
            if posiciones_error.count((i, i)) <= 0:  # Si no se detectó un error longitudinal en esta fila
                #errors += 1
                print(f"Error en paridad VRC en fila {i}")
                if errors > 1:
                    return ""  # No se puede corregir el error
                posiciones_error.append((i, i))  # 'V' para VRC
        else:
            # Si la paridad es correcta, decodifico el caracter
            codigo_ascii = ''.join([str(bit) for bit in fila])  # Convierto la lista de enteros a un string
            caracter = chr(int(codigo_ascii, 2))  # Convierto el codigo ASCII a un caracter
            original_message += caracter
    print(f"Cantidad de errores detectados: {errors}")
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
"""
Probabilidad condicional:
P (A/B) = P (A ∩ B) / P (B) , siempre que P (B) > 0
"""

"""
Un canal de información viene determinado por un
alfabeto de entrada A = {ai}, i = 1, 2, ..., r ; un alfabeto de
salida B = {bj} , j = 1, 2, ..., s ; y un conjunto de
probabilidades condicionales P (bj/ai). Por eso es que apartir de una cadena de entrada y una de salida
se puede obtener la matriz de canal.
PASOS:
1. Identificar los símbolos únicos en las secuencias de entrada y salida.
2. Contar las ocurrencias de cada símbolo de entrada (denominador) y las ocurrencias conjuntas de pares (entrada, salida) (numerador).
3. Calcular las probabilidades condicionales P(bj/ai) y construir la matriz de canal.
"""
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

"""
Las probabilidades de salida de un canal se calculan utilizando las probabilidades a priori de los símbolos de entrada
y la matriz de canal que contiene las probabilidades condicionales P(bj/ai). Ya que la probabilidad de salida P(bj) se obtiene sumando
las contribuciones de todas las entradas posibles ai, ponderadas por sus probabilidades a priori P(ai).
P(bj) = sum_i P(ai) * P(bj/ai)
PASOS:
1. Inicializar una lista para las probabilidades de salida con ceros.
2. Para cada símbolo de salida bj, calcular su probabilidad sumando las contribuciones de todas las entradas ai.
3. Devolver la lista de probabilidades de salida.
"""
def getProbabilidadesSalida(probsPriori: list[float], matrizCanal: list[list[float]]) -> list[float]:
    
    num_simbolos_salida = len(matrizCanal[0])
    probs_salida = [0.0] * num_simbolos_salida

    for j in range(num_simbolos_salida):
        for i in range(len(probsPriori)):
            probs_salida[j] += probsPriori[i] * matrizCanal[i][j]

    return probs_salida
"""
Hace lo mismo que getProbabilidadesSalida pero recibe las cadenas de entrada y salida
y calcula la matriz de canal y las probabilidades a priori internamente.
"""
def getProbabilidadesSalidaConMsg(entrada: str, salida: str) -> list:
    matrizCanal = getMatrizCanal(entrada, salida)
    probsPriori =getAlfabetoyProbabilidades(entrada)[1]
    num_simbolos_salida = len(matrizCanal[0])
    probs_salida = [0.0] * num_simbolos_salida

    for j in range(num_simbolos_salida):
        for i in range(len(probsPriori)):
            probs_salida[j] += probsPriori[i] * matrizCanal[i][j]

    return probs_salida
"""

"""
def getMatrizSucesosSimultaneosConMsg(entrada: str, salida: str) -> list[list[float]]:
    matrizCanal = getMatrizCanal(entrada, salida)
    probsPriori =getAlfabetoyProbabilidades(entrada)[1]
    num_simbolos_salida = len(matrizCanal[0])
    probs_simultaneas = [[0.0] * num_simbolos_salida for _ in range(len(probsPriori))]

    for i in range(len(probsPriori)):
        for j in range(num_simbolos_salida):
            probs_simultaneas[i][j] = probsPriori[i] * matrizCanal[i][j]
 
    return probs_simultaneas

"""
Las probabilidades simultaneas se definen como:
P(ai, bj)= P(ai /bj) * P(bj)= P(bj/ai) * P(ai)
PASOS:
1. Inicializar una matriz para las probabilidades simultáneas con ceros.
2. Para cada par (ai, bj), calcular la probabilidad simultánea multiplicando la probabilidad a priori P(ai)
   por la probabilidad condicional P(bj/ai) de la matriz de canal.
3. Devolver la matriz de probabilidades simultáneas.
"""
def getMatrizSucesosSimultaneos(probsPriori: list[float], matrizCanal: list[list[float]]) -> list[list[float]]:
    num_simbolos_salida = len(matrizCanal[0])
    probs_simultaneas = [[0.0] * num_simbolos_salida for _ in range(len(probsPriori))]

    for i in range(len(probsPriori)):
        for j in range(num_simbolos_salida):
            probs_simultaneas[i][j] = probsPriori[i] * matrizCanal[i][j]

    return probs_simultaneas

"""
Calcula las probabilidades a posteriori P(ai/bj) utilizando el teorema de Bayes:
P(ai/bj) = ( P(bj/ai) * P(ai) ) / P(bj)
PASOS:
1. Inicializar una matriz para las probabilidades a posteriori con ceros.
2. Para cada símbolo de salida bj, calcular las probabilidades a posteriori para cada símbolo de entrada ai.
3. Devolver la matriz de probabilidades a posteriori.
"""
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
"""
H (A/bj) representa el número medio de binits necesarios
para representar un símbolo de una fuente con una probabilidad a posteriori P(ai/bj), i = 1, 2, ..., r.
H (A/bj) =  sum_i P(ai/bj) * log2(1/P(ai/bj))
Incertidumbre promedio sobre la entradas al conocer las salidas
PASOS:
1. Calcular las probabilidades a posteriori P(ai/bj) utilizando el teorema de Bayes.
2. Para cada símbolo de salida bj, calcular la entropía condicional H(A/bj) sumando las contribuciones de todas las entradas ai.
3. Devolver la lista de entropías condicionales H(A/bj).
"""
def getEntropiasAPosteriori(probsPriori: list[float], matrizCanal: list[list[float]]) -> list[list[float]]:
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

"""
Promedio de las incertidumbres de las entradas al conocer las salidas.
Calcula la entropia media a posteriori o la equivocación (ruido) H(A/B) por definición.
La cual mide la informacion que queda en A cuando se conoce B.
Nro. mínimo de preguntas binarias en promedio para determinar la entrada conocida la salida
Pueden haber valores de salida que nno see correspondan a una entrada. Een ese caso de las agrupa
como b = * y como consecuencia la entropía sobre la entrada aumenta H(A/b=*) > H(A)
La equivocacón será siempre menor que la entropía a priori H(A) ya que conocer B reduce la incertidumbre sobre A.
PASOS:
1. Calcular las probabilidades de salida P(B) usando las probabilidades a priori y la matriz de canal.
2. Calcular las probabilidades a posteriori P(A/B) usando el teorema de Bayes.
3. Calcular la matriz de sucesos simultáneos P(A,B).
4. Calcular la equivocación H(A/B) sumando sobre todos los pares (ai, bj) la contribución P(ai, bj) * log2(1/P(ai/bj)).
5. Devolver el valor de la equivocación H(A/B).
"""
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
"""
Calcula la pérdida H(B/A) por definición.
Nro. mínimo de preguntas binarias en promedio para determinar la salida conocida la entrada.
Mide la distorsión que el canal introduce en la información transmitida.
PASOS:
1. Para cada símbolo de entrada ai, calcular la entropía condicional H(B/ai) utilizando la matriz de canal.
2. Multiplicar cada entropía condicional H(B/ai) por la probabilidad a priori P(ai).
3. Sumar todas las contribuciones para obtener la pérdida H(B/A).
4. Devolver el valor de la pérdida H(B/A).
"""
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
"""
Además de las entropías H(A) y H(B), puede definirse la
entropía afín, que mide la incertidumbre del suceso simultáneo (ai, bj)
H (A ,B)=∑ P(a ,b)log (1/P(a,b))
PASOS:
1. Calcular la matriz de sucesos simultáneos P(A,B) utilizando las probabilidades a priori y la matriz de canal.
2. Calcular la entropía afín H(A,B) sumando sobre todos los pares (ai, bj) la contribución P(ai, bj) * log2(1/P(ai, bj)).
3. Devolver el valor de la entropía afín H(A,B).
"""
def getEntropiaAfín(probsPriori: list[float], matrizCanal: list[list[float]]) -> float:
    matrizSimultaneas = getMatrizSucesosSimultaneos(probsPriori, matrizCanal)
    entropiaAfin = 0.0
    for i in range(len(matrizSimultaneas)):
        for j in range(len(matrizSimultaneas[0])):
            entropiaAfin += matrizSimultaneas[i][j] * math.log2(1/matrizSimultaneas[i][j]) if matrizSimultaneas[i][j] > 0 else 0.0
    return entropiaAfin


"""
La informacion mutua es la diferencia entre la entropía a priori y la equivocación H(A/B).
Es decir es la cantidad de informacion logra transmitirse a través del canal.
I(A,B)= H(A)-H(A/B)
I(A, B)=∑P(a , b)log(P(a/b)/P(a)) 
Como P(ai,bj)=P(ai/bj).P(bj):
I(A, B) = ∑ P(a,b) * log2( P(a,b) / (P(a) * P(b)) )
PASOS:
1. Calcular la matriz de sucesos simultáneos P(A,B) utilizando las probabilidades a priori y la matriz de canal.
2. Calcular las probabilidades de salida P(B).
3. Calcular la información mutua I(A,B) sumando sobre todos los pares (ai, bj) la contribución P(ai, bj) * log2( P(ai, bj) / (P(ai) * P(bj)) ).
4. Devolver el valor de la información mutua I(A,B).
"""
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

"""
H(A,B)=H(B)+H(A/B) // la entropía afín se puede expresar como la suma de la entropía de las probabilidades de salida y la equivocación
H(A,B)=H(A)+H(B/A) // o como la suma de la entropía a priori y la pérdida.

"""
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
"""
Verifica si un canal es sin ruido. Al observar una salida bj se conoce con certeza el símbolo ai transmitido,
es decir las probabilidades condicionales P (ai/bj) son 0 y 1. La equivocación H (A/B) es cero.

PASOS:
1. Recorrer cada columna de la matriz del canal.
2. Verificar que cada columna tenga exactamente un valor 1 y el resto sean 0.
"""
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
"""
Verifica si un canal es determinante.
El símbolo de entrada ai es suficiente para determinar, con probabilidad 1, el
símbolo de salida bj. Por lo tanto las probabilidades P(bj/ai) han de ser 0 ó 1,. (al reves que sin ruido)
PASOS:
1. Recorrer cada fila de la matriz del canal.
2. Verificar que cada fila tenga exactamente un valor 1 y el resto sean 0.
"""
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

"""
P (ck/bj, ai) = P (ck/bj) para cualquier i, j, k
P (ai/bj, ck) = P (ai/bj)
Al transmitir una información a través de dos canales en serie parece lógico
que la equivocación aumente, es decir que H (A /C) sea mayor que H (A/B).
Los canales tienden a “perder” información. La información que emerge
finalmente de varios canales en serie no puede ser mayor que la que
emergía de un punto intermedio de la serie, si se pudiera extraer de él.
PASOS:
1. Verificar que el número de columnas del primer canal sea igual al número de filas del segundo canal.
2. Multiplicar las matrices de los dos canales para obtener la matriz del canal compuesto.

"""
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


"""
Verifica si dos columnas de la matriz se pueden combinar en una reducción suficiente.
Dos columnas se pueden combinar si para cada fila los elementos son iguales o multiplicables.
PASOS:
1. Inicialiizar un vector de constantes por las que se multiplican los elementos de una columna para obtener los de la otra.
1. Recorrer cada fila de las dos columnas especificadas.
2. Verificar si ambos elementos son cero. Si es así, comprobar que la lista no esta vacía
   y establecer que entonces los elementos de esta fila también son multiplicables por la misma constante.
3. Si uno de los elementos es cero y el otro no, retornar False.
4. Si ambos elementos son distintos de cero, calcular la constante como el cociente del segundo elemento entre el primero
   y agregarla a la lista de constantes.
5. Después de recorrer todas las filas, verificar si todas las constantes en la lista son iguales (ignorando ceros).
"""
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


"""
Genera la matriz del canal determinante para combinar 'col1' y 'col2'.
La nueva columna combinada estará en el índice 'col1'.
PASOS:
1. Asegurar que col1 sea siempre la más pequeña para que sea el nuevo índice.
2. Inicializar una nueva matriz con el número de filas igual al número de columnas de la matriz original
   y el número de columnas igual al número de columnas de la matriz original menos uno.
3. Mapear las dos columnas a combinar en la nueva matriz.
4. Mapear el resto de columnas (identidad).
"""
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

"""
Realiza reducciones sucesivas suficientes en la matriz del canal hasta que no se puedan hacer más.
PASOS:
1. Inicializar una copia de la matriz original para realizar las reducciones.
2. Utilizar un bucle while para continuar intentando reducciones hasta que no se puedan hacer más.
3. Dentro del bucle while, utilizar bucles for anidados para comprobar cada par de columnas.
4. Si se encuentra un par de columnas reducibles, generar la matriz determinante y actualizar la matriz reducida.
5. Repetir el proceso hasta que no se puedan hacer más reducciones.
"""
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
"""
PASOS:
1. Tomar la primera fila de la matriz como referencia.
2. Recorrer cada fila de la matriz, ordenarla y comparar sus elementos con los de la primera fila ordenada.
3. Si alguna fila no coincide, retornar False.
4. Luego, tomar la primera columna de la matriz como referencia.
5. Recorrer cada columna de la matriz, ordenarla y comparar sus elementos con los de la primera columna ordenada.
6. Si alguna columna no coincide, retornar False.
"""
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

"""
PASOS:
1. Tomar la primera fila de la matriz como referencia.
2. Recorrer cada fila de la matriz, ordenarla y comparar sus elementos con los de la primera fila ordenada.
3. Si alguna fila no coincide, retornar False.
"""
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

"""
Si el canal es BSC y la probabilidad de error es 1 se pueden invertir los bits recibidos para
recuperar la información original sin errores.
PASOS:
1. Verificar que la matriz tenga exactamente 2 filas y 2 columnas.
2. Tomar la probabilidad de error de la primera fila y segunda columna.
3. Comparar esta probabilidad con la probabilidad correspondiente en la segunda fila y primera columna.
4. Si son iguales, retornar True; de lo contrario, retornar False.
"""
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

"""
Es la maxima tasa a la que se puede trannsmitir información de manera confiable a través de ese canal
C=max(I( A, B))
Calcula la capacidad del canal dado su matriz de canal.
Si el canal no entra dentro de ninguno de los casos especiales, se debe maximizar la información mutua
no se realiza en esta funcion.
PASOS:
1. Verificar si el canal es determinante, sin ruido, simétrico, uniforme o BSC.
2. Calcular la capacidad según el tipo de canal identificado.
3. Retornar el valor de la capacidad calculada.
Si intentas transmitir datos a una velocidad mayor que la capacidad,
es matemáticamente imposible reconstruir el mensaje sin errores.
Si transmites por debajo de C, Shannon demostró que siempre existe
un código lo suficientemente inteligente para corregir casi todos los errores.
"""
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


"""
Dado un paso y una matriz de canal binario, estima la capacidad del canal binario.
PASOS:
1. Inicializar variables para almacenar la máxima información mutua y la probabilidad asociada.
2. Iterar sobre las probabilidades a priori desde 0 hasta 1 con el paso especificado.
3. Para cada probabilidad a priori, calcular la información mutua utilizando la función getInformacionMutua.
4. Si la información mutua calculada es mayor que la máxima registrada, actualizar la máxima
   información mutua y la probabilidad asociada.
5. Retornar la máxima información mutua y la probabilidad asociada.
"""
def estimarCapacidadCanalBinario(matriz: list[list[float]], paso: float) -> tuple[float, float]:
    """
    Estima la capacidad de un canal binario mediante el cálculo de la información mutua
    para un conjunto de probabilidades a priori distribuidas uniformemente según el paso especificado.
    Retorna el valor de capacidad estimado junto con su probabilidad asociada.
    """
    maxInfoMutua = 0.0
    probabilidadAsociada = 0.0
    
    p = 0.0
    while p <= 1.0:
        probsPriori = [p, 1 - p]
        infoMutua = getInformacionMutua(probsPriori, matriz)
        
        if infoMutua > maxInfoMutua:
            maxInfoMutua = infoMutua
            probabilidadAsociada = p
            
        p += paso
    
    return maxInfoMutua, probabilidadAsociada

"""
El segundo teorema de Shannon trata de la cantidad de información sin error que puede obtenerse de un
cierto canal.
El valor de la probabilidad de error que corresponde al empleo de una regla de
decisión cualquiera (por ejemplo la regla de máxima probabilidad) viene dado por:
P(e) = ∑ P(ai) ∑ P(bj/ai) ,donde la segunda suma se extiende a todos los bj que no son
decididos como ai.
PASOS:
1. Para cada columna de la matriz, encontrar el índice de la fila con el valor máximo (decisión óptima).
2. Calcular la probabilidad de error sumando las probabilidades de todas las entradas
   (excepto las de los máximos) y afectandola por la probabilidad a priori.
3. Devolver la probabilidad de error calculada.
"""
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