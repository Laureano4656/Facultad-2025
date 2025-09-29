import math
import random

def informacion(probabilidades): #Informacion de cada simbolo calculada a partir de la probabilidad de que este salga
    info = list()
    for prob in probabilidades:
        if prob>0:
            info.append(math.log2(1/prob))
        else:
            info.append(0)
    return info

def entropia(probabilidades): #Entropia de la fuente calculada a partir de las probabilidades de sus simbolos. El valor medio de la información por símbolo suministrada por la fuente
    info = informacion(probabilidades)
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
#
# ##


def cadena_mensaje(cadena): #Genero el alfabeto y las probabilidades de sus simbolos dada una cadena
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

def generar_msj_alfabeto_palabra(alfabeto, probabilidades,n): #Genero un mensaje dado un alfabeto y las probabilidades de sus simbolos. Longitud N
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
    H = entropia([w,1-w])
    return H

def calcular_extension_n(fuente,probabilidades,n): #Calculo extensiones de grado N a partir de la fuente y de las probabilidades
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

def vector_estacionario(matriz,n): #Calculo el vector estacionario (Aproximacion) a partir de la matriz
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
    v0=[round(v,2) for v in v0]
    return v0

##
# La distribucion de probabilidad de los simbolos en la fuente en el vector t va variando con la evolucion del proceso de emision de simbolos. 
# El vector estacionario representa la distribucion de probabilidad a largo plazo, es decir, la distribucion a la que tiende el sistema despues de muchas transiciones.
# El vector estacionario cumple que V*.M = V*, donde M es la matriz de transicion de estados.
# Esto significa que si el sistema alcanza el vector estacionario, permanecerá en ese estado de distribucion de probabilidad en futuras transiciones.
# En resumen, el vector estacionario es una caracteristica fundamental de las cadenas de Markov y es crucial para entender el comportamiento a largo plazo de la fuente con memoria.
##


def entropia_con_vector(matriz,vector_est,n): #Calculo la entropia a partir de una matriz y su vector estacionario
   H=0
   for i in range(n):
       for j in range(n):
           if (matriz[i][j]>0):
                H += vector_est[i]*matriz[j][i]*(-math.log2(matriz[j][i]))
   return round(H, 2)




def generar_matriz(cadena): #Genero la matriz a partir de una cadena dada.
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
                matriz[i][j] = round(matriz[i][j], 2)
    return alfabeto,matriz

##
# Si la cadena dada es lo suficientemente larga, la matriz de transicion de estados generada a partir de ella sera una buena aproximacion de la matriz real de la fuente.
# Si la cadena es corta, la matriz generada puede no reflejar con precision las probabilidades de transicion entre estados.
# Ademas, si la cadena no contiene todas las posibles transiciones entre simbolos del alfabeto, algunas entradas de la matriz seran cero, lo que puede afectar el calculo del vector estacionario y la entropia.
#
##
            
def generar_cadena_matriz(matriz,alfabeto,n): #Genero una cadena a partir de su matriz de markov y alfabeto
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
# La probabilidad
#
#
##

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

def no_singular(codigo): # Un codigo es no singular si todas sus palabras codigo son distintas. Va a ser decodificable pero puede ser ambiguo
  i = 0
  while (i<len(codigo) and codigo.count(codigo[i])==1):
    i+=1
  return i==len(codigo)

def instantaneo(codigo): # Un codigo es instantaneo si ninguna palabra codigo es prefijo de otra palabra codigo. Puede decodificarse a medida que se recibe cada simbolo
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

def univoco(codigo): # Un codigo es univocamente decodificable si cualquier secuencia de simbolos del alfabeto puede ser decodificada de una unica manera
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
        if (instantaneo(codigo)):
            return ("El codigo es instantaneo")  
        else:
            if (univoco(codigo)):
                return ("El codigo es univoco")
            else:
                return ("El codigo es no singular, no instantaneo y no univoco")
            
            
##
# Codigo Bloque o No singular, NO SON DECODIFICABLES
# Codigo Instantaneo, SI SON DECODIFICABLES y ademas se pueden decodificar a medida que se reciben los simbolos
# Codigo Univoco, SI SON DECODIFICABLES pero no se pueden decodificar a medida que se reciben los simbolos, hay que obtener la cadena completa
# Codigo No Singular, No Instantaneo y No Univoco, Son decodificables pero ambiguos, es decir, una misma cadena puede tener mas de una decodificacion posible
##
            
def devolver_alfabeto(palabras_codigo): # Dada una lista de palabras codigo devuelve el alfabeto codigo
    alfabeto = set()
    for palabra in palabras_codigo:
        for caracter in palabra:
            alfabeto.add(caracter)
    return alfabeto

def longitud_palabras(palabras_codigo): # Devuelve una lista con las longitudes de cada palabra codigo
    longitud = list()
    for palabra in palabras_codigo:
        longitud.append(len(palabra))
    return longitud

def in_Kraft(alfabeto,longitud): # Devuelve el valor de realizar la Sumatoria de la Inecuacion de Kraft
    sumatoria = 0
    r = len(alfabeto)
    for i in range(len(longitud)):
        sumatoria += r**(-longitud[i])
    return round(sumatoria, 2) # Si esta es <= 1 entonces el codigo como minimo es Univocamente Decodificable, si no existieran prefijos este seria Instantaneo

##
# La inecuacion de Kraft es una condicion necesaria para que un codigo sea univocamente decodificable. 
# Si la suma es menor o igual a 1, entonces el codigo puede ser instantaneo. 
# Si la suma es mayor a 1, entonces el codigo no sera univocamente decodificable, por ende tampoco sera instantaneo.
# Me asegura la existencia de una combinacion de palabras codigo de las mismas longitudes que las palabras codigo dadas para que el codigo sea instantaneo.
##

def entropia_codigo(palabras_codigo, probabilidad): # Calcula la entropia del codigo, con el logaritmo en base r (Longitud del Alfabeto codigo)
    s = 0
    alfabeto = devolver_alfabeto(palabras_codigo)
    r = len(alfabeto)
    for prob in probabilidad:
        s+=prob*math.log(1/prob,r)
    return round(s,2)

def longitud_media(palabras_codigo, probabilidad): # Calculo la longitud media del codigo
    l = 0
    for i in range(len(palabras_codigo)):
        l += probabilidad[i]*len(palabras_codigo[i])
    return round(l,2)

def codigo_compacto(palabras_codigo, probabilidad): # Dadas las palabras codigo y sus probabilidades se determina si este es compacto mediante el uso de que la Longitud de la palabra codigo sea menor igual a su Informacion
    alfabeto = devolver_alfabeto(palabras_codigo)
    r = len(alfabeto)
    bandera = False
    if (instantaneo(palabras_codigo)):
        bandera=True
        for elemento,prob in zip(palabras_codigo,probabilidad):
            if(not(len(elemento)<=math.ceil(math.log(1/prob,r)))):
                bandera = False
                break
    return bandera

def generar_mensaje_codigo(palabras_codigo, probabilidades, n): # Genera un mensaje codificado a partir de las palabras codigo
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

