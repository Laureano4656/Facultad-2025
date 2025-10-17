import math

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

def getLongitudMedia(palabras_codigo, probabilidad): 
    l = 0
    for i in range(len(palabras_codigo)):
        l += probabilidad[i]*len(palabras_codigo[i])
    return l

def getKraft(alfabeto,longitud): 
    sumatoria = 0
    for i in range(len(longitud)):
        sumatoria += len(alfabeto)**(-longitud[i])
    return sumatoria # Si esta es <= 1 entonces existe un codigo Instantaneo con estas longitudes

def getLongitudesPalabrasCod(codigo): 
    longitud = list()
    for palabra in codigo:
        longitud.append(len(palabra))
    return longitud

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
    return 

dist_prob1 = [0.15,0.25,0.05,0.45,0.1]
cod1 = ["/+","*","+-","-"]
alfabetoCod1 = getAlfabetoCodigo(cod1)

print("Alfabeto codigo 1: ",alfabetoCod1)

print("Entropia codigo 1: ",getEntropiaCodigoR(cod1,dist_prob1))

print("Longitud media codigo 1: ",getLongitudMedia(cod1,dist_prob1))

print("Inecuacion Kraft-Mc Millan: ",getKraft(alfabetoCod1,getLongitudesPalabrasCod(cod1)))

print("El codigo es no singular: ",isNoSingular(cod1))
print("El codigo es unequivoco: ",isUnivoco(cod1))
print("El codigo es instantaneo: ",isInstantaneo(cod1))
print("El codigo es compacto: ",isCompacto(cod1,dist_prob1))

print("-------------------------------------------------")

dist_prob2 = [0.15,0.25,0.05,0.45,0.1]
cod2 = [",;" , ";" , ":." , "." , ",:"]

alfabetoCod2 = getAlfabetoCodigo(cod2)

print("Alfabeto codigo 2: ",alfabetoCod2)

print("Entropia codigo 2: ",getEntropiaCodigoR(cod2,dist_prob2))

print("Longitud media codigo 2: ",getLongitudMedia(cod2,dist_prob2))

print("Inecuacion Kraft-Mc Millan: ",getKraft(alfabetoCod2,getLongitudesPalabrasCod(cod2)))

print("El codigo es no singular: ",isNoSingular(cod2))
print("El codigo es unequivoco: ",isUnivoco(cod2))
print("El codigo es instantaneo: ",isInstantaneo(cod2))
print("El codigo es compacto: ",isCompacto(cod2,dist_prob2))