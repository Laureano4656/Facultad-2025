import math
import random

def getInfo(probabilidades): #Informacion de cada simbolo calculada a partir de la probabilidad de que este salga
    info = list()
    for prob in probabilidades:
        if prob>0:
            info.append(math.log2(1/prob))
        else:
            info.append(0)
    return info

def getEntropia(probabilidades):
    info = getInfo(probabilidades)
    H = 0
    for I,P in zip(info,probabilidades):
        H += I*P
    return H

def getAlfabetoYProbabilidades(cadena): #Genero el alfabeto y las probabilidades de sus simbolos dada una cadena
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

def generarMsj(alfabeto, probabilidades,n): #Genero un mensaje dado un alfabeto y las probabilidades de sus simbolos. Longitud N
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

def prob_w(w): #Calculo entropia de un alfabeto binario a partir de una probabilidad w
    H = getEntropia([w,1-w])
    return H

def calcularExtensionN(fuente,probabilidades,n): #Calculo extensiones de grado N a partir de la fuente y de las probabilidades
    if n == 1:
        return fuente,probabilidades
    else:
        nueva_fuente = []
        nuevas_probabilidades = []
        anterior_fuente,anteriores_probabilidades = calcular_extension_n(fuente,probabilidades,n-1)
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

def getVectorEstacionario(matriz,n): #Calculo el vector estacionario (Aproximacion) a partir de la matriz
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

def getEntropiaMatriz(matriz,vector_est,n) -> float: #Calculo la entropia a partir de una matriz y su vector estacionario
   H=0
   for i in range(n):
       for j in range(n):
           if (matriz[i][j]>0):
                H += vector_est[i]*matriz[j][i]*(-math.log2(matriz[j][i]))
   return H

def generarMatriz(cadena): #Genero la matriz a partir de una cadena dada.
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
            
def generarMsgMatriz(matriz,alfabeto,n): ##Genero una cadena a partir de su matriz de markov y alfabeto
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

def fuente_con_memoria_nula(matriz,tolerancia): #Busca la maxima diferencia entre probabilidades de los simbolos, si esta es mayor a la tolerancia la fuente tiene memoria, sino tiene memoria nula
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

def no_singular(codigo):
  i = 0
  while (i<len(codigo) and codigo.count(codigo[i])==1):
    i+=1
  return i==len(codigo)

def isInstantaneo(codigo):
  band = 1
  i = 0
  while (i<len(codigo) and band):
    j=0
    while (j<len(codigo) and band):
      if (j!=i and codigo[j].startswith(codigo[i])):
        band = 0
      j+=1
    i+=1
  return band

def isUnivoco(codigo):
  S = [set(codigo), set()] # Lista de conjuntos ya vistos
  i = 0 # Numero de Iteraciones
  seguir = True
  while seguir:
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

def tipo_codigo(codigo):
    if (not no_singular(codigo)):
        return ("El codigo es de tipo bloque")
    else:
        if (isInstantaneo(codigo)):
            return ("El codigo es instantaneo")  
        else:
            if (isUnivoco(codigo)):
                return ("El codigo es univoco")
            else:
                return ("El codigo es no singular, no instantaneo y no univoco")
            
def getAlfabetoCodigo(codigo): # Dada una lista de palabras codigo devuelve el alfabeto codigo
    alfabeto = set()
    for elemento in codigo:
        for caracter in elemento:
            alfabeto.add(caracter)
    return alfabeto

def getLongitudes(codigo): # Devuelve una lista con las longitudes de cada palabra codigo
    longitud = list()
    for palabra in codigo:
        longitud.append(len(palabra))
    return longitud

def in_Kraft(alfabeto,longitud): # Devuelve el valor de realizar la Sumatoria de la Inecuacion de Kraft
    sumatoria = 0
    for i in range(len(longitud)):
        sumatoria += len(alfabeto)**(-longitud[i])
    return sumatoria # Si esta es <= 1 entonces el codigo como minimo es Univocamente Decodificable, si no existieran prefijos este seria Instantaneo

# def tipo_codigo_Kraft(codigo):
#     if (not no_singular(codigo)):
#         return ("El codigo es de tipo bloque")
#     else:
#         if (isInstantaneo(codigo)):
#             return ("El codigo es instantaneo")  
#         else:
#             if (in_Kraft(getAlfabetoCodigo(codigo),getLongitudes(codigo))<=1):
#                 return ("El codigo es univoco")
#             else:
#                 return ("El codigo es no singular, no instantaneo y no univoco")

def getEntropiaCodigo(codigo, probabilidad): # Calcula la entropia del codigo, con el logaritmo en base r (Longitud del Alfabeto codigo)
    s = 0
    alfabeto = getAlfabetoCodigo(codigo)
    r = len(alfabeto)
    for prob in probabilidad:
        s+=prob*math.log(1/prob,r)
    return s

def getLongitudMedia(palabras_codigo, probabilidad): # Calculo la longitud media del codigo
    l = 0
    for i in range(len(palabras_codigo)):
        l += probabilidad[i]*len(palabras_codigo[i])
    return l

def isCompacto(palabras_codigo, probabilidad): # Dadas las palabras codigo y sus probabilidades se determina si este es compacto mediante el uso de que la Longitud de la palabra codigo sea menor igual a su Informacion
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

def generateMsgCod(palabras_codigo, probabilidades, n): # Genera un mensaje codificado a partir de las palabras codigo
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
