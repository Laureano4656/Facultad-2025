import math

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

def isMemoriaNula(matriz,tolerancia): 
    maxima_dif = []
    for i in range(len(matriz)):
        maxima_dif.append(max(matriz[i])-min(matriz[i]))
    maxima = max(maxima_dif)
    if maxima<tolerancia:
        return True
    else:
        return False
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
msg1 = "+-/+/-//-/*-/**-*---////-+--*+*/-----/--+/++--*/-+"

alfabeto1,dist_prob1 =getAlfabetoyProbabilidades(msg1)

print("Distribucion de probabilidades mensaje 1: ",dist_prob1)

matMsg1 = getMatriz(alfabeto1,msg1)

print("Alfabeto mensaje 1: ",alfabeto1)

print("Es memoria nula: ",isMemoriaNula(matMsg1,0.01))

print("Matriz mensaje 1")
print(matMsg1)

print("Entropia msg1: ",getEntropia(dist_prob1))

nuevaFuente1,nuevasProbs1 = calcExtensionN(alfabeto1,dist_prob1,2)

print("Alfabeto extension 2: ",nuevaFuente1)
print("Probabilidades extension 2: ",nuevasProbs1)
print("Entropia extension 2: ",getEntropia(nuevasProbs1))

print("--------------------------------------------")

msg2 = "-+-+*//++///*/-////+---////-+/+--+-+/-/+-+/-+*++//"

alfabeto2,dist_prob2 = getAlfabetoyProbabilidades(msg2)
print("Alfabeto mensaje 2: ",alfabeto2)
print("Distribucion de probabilidades mensaje 2: ",dist_prob2)

matMsg2 = getMatriz(alfabeto2,msg2)

print("Matriz de mensaje 2:")

print(matMsg2)

print("Es memoria nula: ",isMemoriaNula(matMsg2,0.01))

print("Entropia msg2: ",getEntropia(dist_prob2))

print("Vector estacionario mensaje 2: ",getVecEstacionarioMat(matMsg2,len(matMsg2)))