import math
import random

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
def getAlfabetoyProbabilidades(cadena):
    alfabeto = list()
    apariciones = list()
    for simbolo in cadena:
        if (simbolo in alfabeto):
            apariciones[alfabeto.index(simbolo)]+=1
        else:
            apariciones.append(1)
            alfabeto.append(simbolo)
    probabilidades = [aparicion/len(cadena) for aparicion in apariciones]
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
