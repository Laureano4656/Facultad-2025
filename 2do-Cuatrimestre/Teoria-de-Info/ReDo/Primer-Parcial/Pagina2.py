import math

def getAlfabetoCodigo(codigo: list[str]) -> set[str]: 
    alfabeto = set()
    for elemento in codigo:
        for caracter in elemento:
            alfabeto.add(caracter)
    return alfabeto

def getEntropiaCodigoR(codigo: list[str], probabilidad: list[float]) -> float:
    s = 0
    alfabeto = getAlfabetoCodigo(codigo)
    r = len(alfabeto)
    for prob in probabilidad:
        s+=prob*math.log(1/prob,r)
    return s

def getLongitudesPalabrasCod(codigo: list[str]) -> list[int]: 
    return [len(cod) for cod in codigo];

def getLongitudMedia(palabras_codigo: list[str], probabilidad: list[float]) -> float: 
    return sum([p * l for p, l in zip(probabilidad, getLongitudesPalabrasCod(palabras_codigo))]);

def getKraft(alfabeto: set[str], longitud: list[int]) -> float: 
    sumatoria = 0
    for i in range(len(longitud)):
        sumatoria += len(alfabeto)**(-longitud[i])
    return sumatoria # Si esta es <= 1 entonces existe un codigo Instantaneo con estas longitudes

def isNoSingular(codigo: list[str]) -> bool:
  i = 0
  while (i<len(codigo) and codigo.count(codigo[i])==1):
    i+=1
  #print(i)
  return i==len(codigo)

def isInstantaneo(codigo: list[str]) -> bool:
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

def isUnivoco(codigo: list[str]) -> bool: # Algoritmo de Sardinas-Patterson
  S = [set(codigo), set()] # Lista de conjuntos ya vistos
  i = 0 # Numero de Iteraciones
  seguir = True
  while seguir:
    #   print(S[i])
      for x in S[0]: # Siempre comparo con el codigo
          for y in S[i]: # En S[i] se guarda el conjunto el cual debo comparar con S[0]
              if x.startswith(y) and x != y:
                  S[i+1].add(x[len(y):])
                #   print("Agrego x:", x[len(y):])
                #   print("x:", x, "y:", y)
              else:
                  if y.startswith(x) and x != y:
                    #   print("Agrego y:", y[len(x):])
                    #   print("x:", x, "y:", y)
                      S[i+1].add(y[len(x):])
    #   print("Siguiente conjunto:", S[i+1])
    #   print("-----")
    #   print(S)
    #   print("-----")
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

def isCompacto(palabras_codigo: list[str], probabilidad: list[float]) -> bool: 
    if not isInstantaneo(palabras_codigo):
        return False;
    r = len(getAlfabetoCodigo(palabras_codigo));
    longitudes = getLongitudesPalabrasCod(palabras_codigo);
    for i in range(len(palabras_codigo)):
        if longitudes[i] > math.ceil(math.log(1/probabilidad[i], r)):
            return False;
    return True;



"""
Para cada uno de los siguientes códigos:
Identificar el alfabeto código
Calcular la entropía de la fuente y la longitud media del código
Comprobar si la codificación cumple la inecuación de Kraft-McMillan
Clasificarlo de acuerdo a sus propiedades
Determinar si se trata de un código compacto
En caso de haber utilizado el algoritmo de Sardinas-Patterson, informar los resultados obtenidos en cada paso
"""
cod1 = ['/+','*','+-','-','*/']
probs1 = [0.15,0.25,0.05,0.45,0.10]

alfabetoCodigo1 = getAlfabetoCodigo(cod1)
entropia1 = getEntropiaCodigoR(cod1,probs1)
longitudMedia1 = getLongitudMedia(cod1,probs1)
kraft1 = getKraft(alfabetoCodigo1,getLongitudesPalabrasCod(cod1))
info1 = getTipoCodigo(cod1)
compacto1 = isCompacto(cod1,probs1)
print("Codigo 1")
print("Alfabeto codigo:", alfabetoCodigo1)
print("Entropia:", entropia1)
print("Longitud media:", longitudMedia1)
print("Kraft:", kraft1)
print("Tipo de codigo:", info1)
print("Es compacto?:", compacto1)

cod2 = [",;",";",":.",".",",:"]
probs2 = [0.15,0.25,0.05,0.45,0.10]
alfabetoCodigo2 = getAlfabetoCodigo(cod2)
entropia2 = getEntropiaCodigoR(cod2,probs2)
longitudMedia2 = getLongitudMedia(cod2,probs2)
kraft2 = getKraft(alfabetoCodigo2,getLongitudesPalabrasCod(cod2))
info2 = getTipoCodigo(cod2)
compacto2 = isCompacto(cod2,probs2)
print("\nCodigo 2")
print("Alfabeto codigo:", alfabetoCodigo2)
print("Entropia:", entropia2)
print("Longitud media:", longitudMedia2)
print("Kraft:", kraft2)
print("Tipo de codigo:", info2)
print("Es compacto?:", compacto2)