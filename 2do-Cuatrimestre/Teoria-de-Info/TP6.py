import TP5 as utils
print("-----------------------------------------------")
print("TP6")
print("-----------------------------------------------")
'''
b. Informar si es un canal sin ruido y/o determinante
c. Calcular el ruido, la pérdida y la información mutua del canal
'''


'''
Realizar funciones booleanas en Python que reciban como parámetro la matriz de un canal
y verifiquen si se trata de:
a. Un canal sin ruido
b. Un canal determinante
'''

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


C1 = [
    [0.0, 1, 0],
    [0, 0, 1],
    [0, 1, 0],
    [1, 0, 0]
    ]
C2 = [
    [1, 0, 0, 0],
    [0, 0.2, 0, 0.2],
    [0, 0, 1, 0]
]

C3 = [
    [0.3, 0.5, 0.2],
    [0.2, 0.3, 0.5],
    [0.5, 0.2, 0.3]
]

C4 = [
    [0, 0, 1, 0],
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 1]
    ]
probsPrioriC1 = [0.25, 0.25, 0.25, 0.25]
probsPrioriC2 = [0.33, 0.33, 0.34]
probsPrioriC3 = [0.33, 0.33, 0.34]
probsPrioriC4 = [0.25, 0.25, 0.25, 0.25]
print("Canal C1")
print("Sin ruido:", isSinRuido(C1))
print("Determinante:", isDeterminante(C1))
print("Información mutua:", utils.getInformacionMutua( probsPrioriC1, C1))

print("Canal C2")
print("Sin ruido:", isSinRuido(C2))
print("Determinante:", isDeterminante(C2))
#print("Información mutua:", utils.getInformacionMutua( probsPrioriC2, C2))

print("Canal C3")
print("Sin ruido:", isSinRuido(C3))
print("Determinante:", isDeterminante(C3))
#print("Información mutua:", utils.getInformacionMutua( probsPrioriC3, C3))
print("Canal C4")
print("Sin ruido:", isSinRuido(C4))
print("Determinante:", isDeterminante(C4))
#print("Información mutua:", utils.getInformacionMutua( probsPrioriC4, C4))

print("--------------------------------")
'''
Ejercicio 3
a. Determinar la equivocación y la información mutua de cada canal
b. Obtener la matriz del canal compuesto
c. Calcular la equivocación y la información mutua del canal compuesto
d. Comparar los resultados obtenidos en cada caso
'''
print("Ejercicio 3")
canal1 = [
    [0.7,0.0,0.3,0.0],
    [0.2,0.6,0.0,0.2]
]
canal2 = [
    [0.9, 0.0, 0.1],
    [0.0, 1.0, 0.0],
    [0.1, 0.1, 0.8],
    [0.0, 0.5, 0.5]
]

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
        print(canalCompuesto[i])
    return canalCompuesto

print("Canal 1")
probsPrioriCanal1 = [0.5, 0.5]
equivocacion1 = utils.getEquivocacionRuido(probsPrioriCanal1, canal1)
infoMutua1 = utils.getInformacionMutua(probsPrioriCanal1, canal1)
print("Equivocación:", equivocacion1)
print("Información mutua:", infoMutua1)
probsPrioriCanal2 = utils.getProbabilidadesSalida(probsPrioriCanal1, canal1)
print("Canal 2")
equivocacion2 = utils.getEquivocacionRuido(probsPrioriCanal2, canal2)
infoMutua2 = utils.getInformacionMutua(probsPrioriCanal2, canal2)
print("Equivocación:", equivocacion2)
print("Información mutua:", infoMutua2)


canalCompuesto = getCanalCompuesto(canal1, canal2)
print("Canal Compuesto")

probsPrioriCanalCompuesto = [0.5, 0.5]
equivocacionCompuesto = utils.getEquivocacionRuido(probsPrioriCanalCompuesto, canalCompuesto)
infoMutuaCompuesto = utils.getInformacionMutua(probsPrioriCanalCompuesto, canalCompuesto)
print("Equivocación del canal compuesto:", equivocacionCompuesto)
print("Información mutua del canal compuesto:", infoMutuaCompuesto)

print("--------------------------------")
'''
Ejercicio 6
Desarrollar funciones en Python que reciban como parámetros: la matriz de un canal y los
índices de dos columnas, y realicen lo siguiente:
a. Verificar si las columnas se pueden combinar en una reducción suficiente
b. Generar la matriz del canal determinante necesario para combinar las columnas
'''

def verificarColumnasReducibles(matriz: list[list[float]], col1: int, col2: int) -> bool:
    """
    Verifica si dos columnas de la matriz se pueden combinar en una reducción suficiente.
    Dos columnas se pueden combinar si para cada fila los elementos son iguales o multiplicables.
    Debo considerar numeros flotantes.
    Ejemplo:
    0.4 y 0.6 son multiplicables (0.6 es 1.5 * 0.4)
    """
    constantList = [0 for _ in range(len(matriz))]
    for i in range(len(matriz)):
        val1 = matriz[i][col1]
        val2 = matriz[i][col2]
        if val1 == 0 and val2 == 0:
            constantList[i] = 0
        elif val1 == 0 or val2 == 0:
            return False
        else:
            constantList[i] = val2 / val1
    
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
    Genera la matriz del canal determinante necesario para combinar dos columnas.
    """
    print("Generando matriz determinante para combinar columnas", col1, "y", col2)
    cantFilas = len(matriz)
    cantColumnas = len(matriz[0]) - 1 # una columna menos para la nueva columna combinada

    # debo crear una matriz identidad de tamaño cantFilas x cantColumnas
    nuevaMatriz = [[0 for _ in range(cantColumnas)] for _ in range(cantFilas)]

    for i in range(len(nuevaMatriz)):
        nuevaMatriz[i][i] = 1

    # ahora debo realizar una matriz para que cuando la multiplique por la matriz original
    # combine las columnas col1 y col2 en una sola columna
    for i in range(cantFilas):
        if matriz[i][col1] != 0 or matriz[i][col2] != 0:
            nuevaMatriz[i][col1] = 1
            nuevaMatriz[i][col2] = 0

    print("Matriz determinante generada:")
    for fila in nuevaMatriz:
        print(fila)
    return nuevaMatriz

C1 = [
    [0.4, 0.6, 0.0, 0.0],
    [0.0, 0.0, 0.5, 0.5],
    [0.0, 0.0, 0.7, 0.3]
]
C2 = [
    [0.2, 0.3, 0.5],
    [0.0, 0.0, 1.0],
    [0.0, 0.0, 1.0]
]
C3 = [
    [0.4, 0.0, 0.2, 0.4],
    [0.4, 0.3, 0.2, 0.1],
    [0.0, 0.3, 0.0, 0.7]
]
C4 = [
    [0.0, 0.5, 0.0, 0.5],
    [0.8, 0.0, 0.2, 0.0],
    [0.0, 0.5, 0.0, 0.5],
    [0.8, 0.0, 0.2, 0.0]
]

'''
Codificar una función en Python que reciba como parámetro la matriz de un canal y,
utilizando las funciones de los ejercicios 4 y 6, realice todas las reducciones suficientes
posibles y devuelva la matriz del canal reducido.
'''
def maxReduccion(matriz: list[list[float]]) -> list[list[float]]:
    matrizReducida = matriz.copy()
    for i in range(len(matriz)):
        for j in range(len(matriz[0])-1):
            if verificarColumnasReducibles(matrizReducida,j,j+1):
                matrizDeterminante = generarMatrizDeterminante(matrizReducida,j,j+1)
                matrizReducida = getCanalCompuesto(matrizReducida, matrizDeterminante)
    return matrizReducida

print("Reducción de canal C1")
print("Matriz original:")
for fila in C1:
    print(fila)
matrizReducidaC1 = maxReduccion(C1)
print("Matriz reducida:")
for fila in matrizReducidaC1:
    print(fila)