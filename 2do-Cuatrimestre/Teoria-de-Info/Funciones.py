import math;
import random;

######################## TRABAJO PRACTICA N°2 ##########################

# Calcula la cantidad de informacion de cada simbolo en una base r
# Cuidado con esta variante, no siempre r es la longitud del alfabeto
# si calculo la informacion de una extension, r es la longitud del alfabeto original
# r me determina la unidad de la informacion
# Valdra la longitud del alfabeto si estoy calculando la inecuacion de kraft o 
# buscando algun codigo compacto
def calcularInformacion(probabilidades, r):
    return [math.log(1/p, r) for p in probabilidades]




# Calcula la entropia de una fuente de informacion
def calcularEntropia(probabilidades, cantInformacion):
    return sum([p * i for p, i in zip(probabilidades, cantInformacion)]);




# Obtiene el alfabeto de una cadena
def obtenerAlfabeto(cadena):
    alfabeto = [];
    for c in cadena:
        if c not in alfabeto:
            alfabeto.append(c);
    return sorted(alfabeto);




# Calcula las probabilidades de los simbolos en una cadena
def calcularProbabilidades(cadena, alfabeto):
    probabilidad = [];
    total_caracteres = len(cadena);
    for c in alfabeto:
        probabilidad.append(cadena.count(c) / total_caracteres);
    return probabilidad;




# Genera una cadena aleatoria dada un alfabeto y sus probabilidades
def generarCadena(alfabeto, probabilidades, n):
    # Hago un arreglo con las probabilidades acumuladas
    probabilidades_acumuladas = [];
    probabilidades_acumuladas.append(probabilidades[0]);
    for i in range(1, len(probabilidades)):
        probabilidades_acumuladas.append(probabilidades[i] + probabilidades_acumuladas[i-1]);
    cadena = "";
    for i in range(1, n):
        aux = random.random();
        j = 0;
        while(aux > probabilidades_acumuladas[j]):
            j += 1;
        cadena += alfabeto[j];
    return cadena;




# Calcula la entropia de una fuente de informacion binaria
def calcularEntropiaConW(w):
    probabilidades = [w, 1 - w];
    cantInformacion = calcularInformacion(probabilidades, 2);
    return calcularEntropia(probabilidades, cantInformacion);



#Generar alfabeto de extension de orden n
def generarAlfabetoExtension(alfabeto, n):
    if(n == 1):
        return alfabeto;
    else:
        alf_ant = generarAlfabetoExtension(alfabeto, n - 1);
        alf_nuevo = [];
        for sim_ant in alf_ant:
            for sim in alfabeto:
                alf_nuevo.append(sim_ant + sim);
        return alf_nuevo;




def generarProbabilidadesAlfabetoExtension(probabilidades, n):
    if n == 1:
        return probabilidades;
    else:
        prob_ant = generarProbabilidadesAlfabetoExtension(probabilidades, n - 1);
        prob_nueva = [];
        for p1 in prob_ant:
            for p2 in probabilidades:
                prob_nueva.append(p1 * p2);
        return prob_nueva;




def generarVectorEstacionario(mat):
    # Inicializar vector estacionario suponiendo equiprobabilidad
    vec_est = [];
    for i in range(len(mat)): # Len devuelve el numero de filas
        vec_est.append(1/len(mat));
    vec_est_nuevo = [0] * len(mat); # Inicializo todo el vector auxiliar en 0

    # Iterar hasta convergencia
    iteraciones = 100;
    for k in range(iteraciones):
        for i in range(len(mat)):
            vec_est_nuevo[i] = 0;
            for j in range(len(mat)):
                vec_est_nuevo[i] += vec_est[j] * mat[i][j];
        vec_est = vec_est_nuevo[:]; # Hago una copia para no tener referencias
    return vec_est;

#Ej
# mat = 1/2 1/3 0    v = 1/3
#       1/2 1/3 1        1/3
#       0   1/3 0        1/3

# En la primera iteracion queda asi:
# v[0] = 1*2 * 1/3 + 1/3 * 1/3 + 0 * 1/3 = 5/18
# v[1] = 1/2 * 1/3 + 1/3 * 1/3 + 1 * 1/3 = 11/18
# v[2] = 0 * 1/3   + 1/3 * 1/3 + 0 * 1/3 = 1/9
# v = 5/18 11/18 1/9

# IMPORTANTE!!!!!!!!!!!!!
# Este algoritmo funciona para matrices cuyas columnas suman 1
# Lo que hace es recorrer fila por fila y por cada valor de la columna
# tambien avanzo en el vector estacionario y voy multiplicando y sumando




def calcularEntropiaFuenteMarkov(mat, vec_est):
    entropia = 0;
    for j in range(len(mat)):
        sum = 0;
        for i in range(len(mat)):
            if mat[i][j] != 0:
                sum += mat[i][j] * math.log2(1/mat[i][j]); # Esta en base 2
        entropia += vec_est[j] * sum;
    return entropia;




# Genera la matriz tomando el estado actual como las columnas y el siguiente como las filas
def generarMatrizTransicion(mensaje, alfabeto):
    n = len(alfabeto);
    mat = [];

    # Inicializo la matriz en 0
    for i in range(n):
        mat.append([0] * n);

    for j in alfabeto:
        for i in alfabeto:
            aux = j + i;
            for k in range(len(mensaje) - 1):
                if mensaje[k] + mensaje[k + 1] == aux:
                    mat[alfabeto.index(i)][alfabeto.index(j)] += 1;
    
    for j in range(n):
        sum = 0;
        for i in range(n):
            sum += mat[i][j];
        if sum != 0:
            for i in range(n):
                mat[i][j] = round(mat[i][j] / sum, 2);
    return mat;






def simularFuenteMarkov(mat, alfabeto, n):
    # Selecciono un simbolo inicial al azar
    simbolo = random.choice(alfabeto);
    cadena = simbolo;

    # Genero las siguientes 9 iteraciones
    for i in range(1, n):
        # Selecciono el simbolo inicial
        j = alfabeto.index(simbolo);

        # Genero las probabilidades acumuladas de la columna j
        vector_aux = [fila[j] for fila in mat];
        probabilidades_acumuladas = [];
        probabilidades_acumuladas.append(vector_aux[0]);
        for i in range(1, len(vector_aux)):
            probabilidades_acumuladas.append(vector_aux[i] + probabilidades_acumuladas[i-1]);

        # Selecciono un numero random y busco en que intervalo cae
        aux = random.random();
        k = 0;
        while(aux > probabilidades_acumuladas[k]):
            k += 1;

        # Actualizo el simbolo
        simbolo = alfabeto[k];

        cadena += simbolo;

    return cadena;




# Verifica si una fuente es de memoria nula a partir de la matriz de transicion y una tolerancia
def esFuenteMemoriaNula(mat, tolerancia):
    for i in range(len(mat)):
        if max(mat[i]) - min(mat[i]) > tolerancia:
            return False;
    return True;




# Una condicion para que una fuente de Markov sea ergodica
# es que todos los estados sean alcanzables desde algun otro

def esFuenteErgodica(mat):
    for j in range(len(mat)):
        cont = 0;
        for i in range(len(mat)):
            cont += mat[i][j] == 0;
        if cont == len(mat) or (cont == len(mat) - 1 and mat[j][j] != 0): # Si una columna esta llena de 0s o tiene n - 1 0s y de ese estado voy al mismo estado, entonces es no ergodica
            return False;
    return True;


# Analizar si la matriz es ergodica o no
def esFuenteErgodica(matriz, tol = 1e-6):
    """
    Determina si una fuente de Markov es ergódica.
    La matriz debe tener columnas que sumen 1.
    
    Retorna True si es ergódica, False en caso contrario.
    """
    N = len(matriz)
    
    # Generar matriz de conectividad: 1 si hay transición posible, 0 si no
    alcanzable = [[1 if matriz[i][j] > tol else 0 for j in range(N)] for i in range(N)]
    
    # Propagamos conexiones hasta N-1 pasos
    for _ in range(N - 1):
        nueva_conectividad = [[0] * N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                # j es alcanzable desde i si existe k tal que i->k y k->j
                for k in range(N):
                    if alcanzable[i][k] and alcanzable[k][j]:
                        nueva_conectividad[i][j] = 1
                        break  # suficiente con un camino
        alcanzable = nueva_conectividad
    
    # Si hay algún par de estados que no se alcanza, no es ergódica
    for i in range(N):
        for j in range(N):
            if alcanzable[i][j] == 0:
                return False
    return True










############################ TRABAJO PRACTICO N°3 #############################

def esNoSingular(codigo):
    flag = True;
    i = 0;
    while flag and i < len(codigo):
        if codigo.count(codigo[i]) > 1:
            flag = False;
        i += 1;
    return flag;




# Version mia
def esInstantaneo(codigo):
    for i in range(len(codigo)):
        for j in range(i,len(codigo)):
            if i != j:
                if codigo[i].startswith(codigo[j]) or codigo[j].startswith(codigo[i]):
                    return False
    return True




# Version de Tato, Lau y Tino
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




def algoritmoSardinasPetterson(codigo):
    # Devuelve true si el codigo es UD
    # Devuelve false si el codigo no es UD
    S1 = set(codigo);
    S = [];
    S.append(S1); # S1 = S[0]
    i = 0;
    aux = True;
    while aux:
        S.append(set()); # Declaro un nuevo conjunto
        for x in S1:
            for y in S[i]:
                if x.startswith(y):
                    sufijo = x[len(y):];
                    if sufijo != "":
                        S[i+1].add(sufijo);
                else:
                    if y.startswith(x):
                        sufijo = y[len(x):];
                        if sufijo != "":
                            S[i+1].add(sufijo);
        # S[i+1] contiene los sufijos del nuevo conjunto
        if S[i+1].intersection(codigo) != set(): # Si este nuevo conjunto tiene elementos en comun con el codigo, no es UD
            aux = False;
            esUD = False;
        else:
            l = 0;
            while l <= i and S[l] != S[i+1]: # Busco si mi nuevo conjunto ya estaba (Desde 0 a i)
                l += 1;
            if l <= i: # Si algun conjunto es mi nuevo conjunto, entonces es UD
                aux = False;
                esUD = True;
        i += 1;
    return esUD;




# Obtener el alfabeto de un codigo
def getAlfabeto(codigo):
    alfabeto = [];
    for palabra in codigo:
        for simbolo in palabra:
            if simbolo not in alfabeto:
                alfabeto.append(simbolo);
    return alfabeto;




def longitudPalabras(codigo):
    return [len(cod) for cod in codigo];




def calcularSumatoriaKraft(longitudes, r):
    suma = 0;
    for l in longitudes:
        suma += r**(-l); 
    return suma;




def longitudMedia(probabilidades, longitudes):
    return sum([p * l for p, l in zip(probabilidades, longitudes)]);




def esCompacto(codigo, probabilidades):
    if not esInstantaneo(codigo):
        return False;
    r = len(getAlfabeto(codigo));
    longitudes = longitudPalabras(codigo);
    for i in range(len(codigo)):
        if longitudes[i] > math.ceil(math.log(1/probabilidades[i], r)):
            return False;
    return True;




def generarMensajeCodificado(codigo, probabilidades, n):
    probabilidades_acumuladas = [];
    probabilidades_acumuladas.append(probabilidades[0]);
    for i in range(1, len(probabilidades)):
        probabilidades_acumuladas.append(probabilidades[i] + probabilidades_acumuladas[i-1]);
    cadena = "";
    for i in range(1, n):
        aux = random.random();
        j = 0;
        while(aux > probabilidades_acumuladas[j]):
            j += 1;
        cadena += codigo[j];
    return cadena;







################################# TRABAJO PRACTICO N°4 #####################################

def cumplePrimerTeoremaShanon(probabilidades, palabras, n):
    '''
        Probabilidades es la probabilidad de cada simbolo de la fuente original
        (La entropia que calculo es sobre la fuente original)
        Palabras es el codigo para la extension de orden n de la fuente original
        n es la extension que quiero analizar

        La longitud media que calculo es sobre la extension de la fuente
        (Uso las probabilidades de la extension)


        #################### CONSULTA #####################
        ¿Por que uso las probabilidades de la extension pero las longitudes del codigo que me dan?
        ¿Y por que eso da la longitud media de la extension?

        Es asi por la definicion de longitud media, se usa la probabilidad de la fuente
        y la longitud de las palabras del codigo que uso para codificar esa fuente
    '''
    r = len(getAlfabeto(palabras));
    longitudes = longitudPalabras(palabras);
    longitud_media = longitudMedia(generarProbabilidadesAlfabetoExtension(probabilidades, n), longitudes);
    entropia = calcularEntropia(probabilidades, calcularInformacion(probabilidades, r));
    return longitud_media / n >= entropia and longitud_media / n < entropia + 1/n;



def calcularRendimiento(probabilidades, codigo):
    '''
        Probabilidades es la probabilidad de cada simbolo de la fuente original
        Codigo es el codigo para la fuente original
    '''
    r = len(getAlfabeto(codigo));
    longitudes = longitudPalabras(codigo);
    longitud_media = longitudMedia(probabilidades, longitudes);
    entropia = calcularEntropia(probabilidades, calcularInformacion(probabilidades, r));
    return entropia / longitud_media;



def calcularRedundancia(probabilidades, codigo):
    '''
        Probabilidades es la probabilidad de cada simbolo de la fuente original
        Codigo es el codigo para la fuente original
    '''
    return 1 - calcularRendimiento(probabilidades, codigo);



def generarCodigoHuffman(probabilidades):
    lista = [[p, [i]] for i, p in enumerate(probabilidades)];
    lista = sorted(lista, key=lambda x: x[0], reverse=True);
    codigo = [""] * len(probabilidades);
    n = len(probabilidades);
    while n > 1:
        ult = lista.pop(n - 1); # Me quedo con el ultimo
        antUlt = lista.pop(n - 2); # Me quedo con el anteultimo
        aux = [antUlt[0] + ult[0], antUlt[1] + ult[1]]; # Genero aux con la suma de las probabilidades y la union de los indices
        lista.append(aux);
        lista = sorted(lista, key=lambda x: x[0], reverse=True);
        for i in antUlt[1]:
            codigo[i] = "1" + codigo[i]; # Por convencion, a los elementos del vector de indices del antUlt les agrego un 1
        for i in ult[1]:
            codigo[i] = "0" + codigo[i]; # Por convencion, a los elementos del vector de indices del ult les agrego un 0
        n -= 1;
    return codigo;

############### CONSULTAR ###############
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



# Version Valen
def initializeShannonFano ( P: list ) -> list:
    return sorted([ [pi, i] for i, pi in enumerate(P) ], key=lambda item: item[0], reverse=True)


def propagateSubfix( result: list, P: list[list], fix: str ) -> list:
    for pi, i in P:
        result[i] +=  fix 

def shannonfanoAlgorithm ( result: list, Pindex: list  ):
    if len(Pindex) <= 1:
        return

    # calculate split
    total = sum( [ pi for pi, i in Pindex ]) / 2 

    acum = 0
    lastDif = 1 
    splitLocation = -1


    for i, pi in enumerate(Pindex):
        acum += pi[0]

        if acum >= total:
            if min(lastDif, abs(total - acum)) == lastDif:
                splitLocation = i
            else:
                splitLocation = i + 1
            
            firstPart = Pindex[:splitLocation]
            secondPart = Pindex[splitLocation:]

            propagateSubfix( result, firstPart, '1' )
            propagateSubfix( result, secondPart, '0' )

            shannonfanoAlgorithm( result, firstPart)
            shannonfanoAlgorithm( result, secondPart)

            return
                
        lastDif = total - acum

# def shannonfano( S: list, P: list ) -> list:
#     result = [''] * len(S)
#     Pindex = initializeShannonFano(P)
#     shannonfanoAlgorithm(result, Pindex)
#     return result

def shannonfano(P: list) -> list:
    result = [''] * len(P)
    Pindex = initializeShannonFano(P)
    shannonfanoAlgorithm(result, Pindex)
    return result





def codificarMensaje(mensaje, fuente, codigo):
    """
        Dado un mensaje, su fuente y un codigo (Codificado en binario), devuelve el 
        mensaje codificado usando ByteArray, esto es una secuencia de bytes que 
        representan el mensaje. Se usa ByteArray para ahorrar espacio, ya que un 
        string de 0s y 1s ocupa mucho.

        Si me dicen que codifique un mensaje en binario no debe 
        ser asi: "1111" ya que eso ocuparia 4 bytes

        Deberia ser:
        bytearray([15]) ya que 15 en binario es 1111 y eso ocupa 1 byte

        Cada elemento del ByteArray es un byte (8 bits) y es un numero entre 0 y 255
        Esos enteros estan en base 2 ya que es mas util ver un mensaje codificado
        como una secuencia de bits y no de numeros enteros

        Esta funcion devuelve un ByteArray y la longitud del mensaje codificado en bits
        ya que al codificar, para completar el ultimo byte, se pueden agregar bits de relleno (0s). 
    """
    mensaje_codificado = "";
    for simbolo in mensaje:
        indice = fuente.index(simbolo);
        mensaje_codificado += codigo[indice];

    longitud_codificado_bits = len(mensaje_codificado); # La longitud del mensaje codificado en bits

    # Ahora convierto el string de 0s y 1s en un ByteArray
    n = len(mensaje_codificado);
    # Agrego 0s al final para que la longitud sea multiplo de 8
    while n % 8 != 0:
        mensaje_codificado += "0";
        n += 1;
    byte_array = bytearray();
    for i in range(0, n, 8): # Recorro de a 8
        byte = mensaje_codificado[i:i+8]; # Tomo 8 bits
        byte_array.append(int(byte, 2)); # Convierto el string de 8 bits a un numero entero en base 2 y lo agrego al ByteArray
    return byte_array, longitud_codificado_bits;



def decodificarMensaje(mensaje_codificado, fuente, codigo, longitud_original_bits = None):
    """
        Dado un mensaje codificado en binario (ByteArray), su fuente y un codigo 
        (Codificado en binario), devuelve el mensaje decodificado.

        Si se proporciona la longitud original, se utiliza para determinar el final del mensaje.
        Esto es ya que al codificar, para completar el ultimo byte, se pueden agregar bits de relleno (0s).
        Eso me agrega simbolos al final

        El mensaje codificado es un ByteArray, lo convierto a un string de 0s y 1s
        para poder decodificarlo.

        Pasos:
        1. Convertir el ByteArray a un string de 0s y 1s
        2. Recorrer el string de 0s y 1s y buscar las palabras del codigo
        3. Si encuentro una palabra, agrego el simbolo correspondiente al mensaje decodificado
           y avanzo la posicion en el string de 0s y 1s la longitud de la palabra
        4. Si no encuentro ninguna palabra, termino
    """
    mensaje_binario = "";
    for byte in mensaje_codificado:
        mensaje_binario += format(byte, '08b'); # Convierto cada byte a un string de 8 bits y lo agrego al string

    mensaje_decodificado = "";
    i = 0;
    longitud = longitud_original_bits if longitud_original_bits is not None else len(mensaje_binario);
    while i < longitud:
        for j in range(len(codigo)):
            palabra = codigo[j];
            if mensaje_binario.startswith(palabra, i): # Si el mensaje empieza con la palabra en la posicion i
                mensaje_decodificado += fuente[j];
                i += len(palabra); # Avanzo i la longitud de la palabra
                break; # Salgo del for para no seguir buscando
        else:
            # Si no encontre ninguna palabra que coincida, salgo del while
            break;
    return mensaje_decodificado;



def calcularTasaCompresion(mensaje_original, mensaje_codificado):
    tamanio_original = len(mensaje_original) * 8; # Tamaño en bits del mensaje original
    tamanio_codificado = len(mensaje_codificado) * 8; # Tamaño en bits del mensaje codificado
    return tamanio_original / tamanio_codificado;


def comprimirRLC(mensaje):
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



def distanciaHamming(codigo):
    distancia_min = 99999;
    dist = 0;
    if codigo == []:
        return 0;

    for i in range(len(codigo)):
        palabra1 = codigo[i];
        for j in range(i + 1, len(codigo)):
            palabra2 = codigo[j];
            dist = 0;
            for k in range(len(palabra1)):
                if palabra1[k] != palabra2[k]:
                    dist += 1;
            if dist < distancia_min and dist != 0:
                    distancia_min = dist;
        return distancia_min;


def cantErroresDetectados(codigo):
    d = distanciaHamming(codigo);
    if d == 0:
        return 0;
    return d - 1;


def cantErroresCorregibles(codigo):
    d = distanciaHamming(codigo);
    if d == 0:
        return 0;
    return (d - 1) // 2;


def agregarBitParidadPalabra(palabra):
    """
        Recibe una palabra (string de 0s y 1s)
        Si la cantidad de 1s es par agrego un 0 al final
        Si la cantidad de 1s es impar agrego un 1 al final
        Agrega el bit a la palabra
        Devuelve la palabra con el bit de paridad agregado
    """
    cantidad_1s = palabra.count('1');
    if cantidad_1s % 2 == 0:
        return palabra + '0'; # Agrego un 0 si la cantidad de 1s es par
    else:
        return palabra + '1'; # Agrego un 1 si la cantidad de 1s es impar


def agregarBitParidad(codigo):
    """
        Recibe un codigo (lista de strings de 0s y 1s)
        Si la cantidad de 1s es par agrego un 0 al final
        Si la cantidad de 1s es impar agrego un 1 al final
        Agrega el bit a cada palabra del codigo
        Devuelve el codigo con los bits de paridad agregados
    """
    codigo_con_paridad = [];
    for palabra in codigo:
        codigo_con_paridad.append(agregarBitParidadPalabra(palabra));
    return codigo_con_paridad;


def byteCodigoAscii(caracter):
    """
        Dado un caracter, obtengo su codigo ASCII y lo paso a binario en 
        7 bits, eso me da un string y le agrego un bit de paridad al final
        Luego lo devuelvo como un byte (entero en base 2)
    """
    codigo_ascii = format(ord(caracter), '07b');
    print(codigo_ascii);
    codigo_ascii = agregarBitParidadPalabra(codigo_ascii);
    print(codigo_ascii);
    return int(codigo_ascii, 2);


def tieneErrores(byte):
    """
        Dado un byte (entero en base 2), lo convierto a un string de 8 bits
        y verifico si tiene errores usando el bit de paridad
        Devuelvo True si tiene errores, False si no tiene errores

        ############# CONSULTA #############
        ¿Como detecto varios errores en una sola palabra, que hago si el bit coincide
        pero habia mas errores?
    """
    codigo_binario = format(byte, '08b');
    cantidad_1s = codigo_binario.count('1');
    if(codigo_binario[-1] == '1'):
        cantidad_1s -= 1;
    return cantidad_1s % 2 == 0 and codigo_binario[-1] != '0';


def agregarBitParidadVRC(matriz):
    """
        Recibe una matriz (lista de listas) de bits (0s y 1s)
        Agrega una fila al inicio con los bits de paridad VRC
        Devuelve la matriz con la fila de paridad agregada

        Para usar esta funcion, la matriz debe tener 
        la paridad por palabra ya agregada
    """
    fila_paridad = [];
    for j in range(len(matriz[0])):
        cantidad_1s = 0;
        for i in range(len(matriz)):
            if matriz[i][j] == 1:
                cantidad_1s += 1;
        if cantidad_1s % 2 == 0:
            fila_paridad.append(0); # Agrego un 0 si la cantidad de 1s es par
        else:
            fila_paridad.append(1); # Agrego un 1 si la cantidad de 1s es impar
    matriz_con_paridad = [fila_paridad] + matriz; # Agrego la fila de paridad al inicio
    return matriz_con_paridad;


def generarMatrizParidad(mensaje):
    """
        Dado un mensaje (string), genero la matriz de paridad VRC
        Devuelvo la matriz de paridad VRC

        Cada fila es una palabra del mensaje en binario con su bit de paridad
        La primera fila es la fila de paridad VRC
    """
    matriz = [];
    for caracter in mensaje:
        codigo_ascii = format(ord(caracter), '07b'); # Obtengo el codigo ASCII en binario de 7 bits
        codigo_ascii_con_paridad = agregarBitParidadPalabra(codigo_ascii); # Agrego el bit de paridad
        fila = [int(bit) for bit in codigo_ascii_con_paridad]; # Convierto el string a una lista de enteros
        matriz.append(fila);
    matriz_con_paridad = agregarBitParidadVRC(matriz); # Agrego la fila de paridad VRC
    return matriz_con_paridad;



def mensajeMatrizParidad(matriz):
    mensaje = "";
    for i in range(1, len(matriz)): # Empiezo desde 1 para saltar la fila de paridad VRC
        fila = matriz[i];
        codigo_ascii_con_paridad = ''.join([str(bit) for bit in fila]); # Convierto la lista de enteros a un string
        codigo_ascii = codigo_ascii_con_paridad[:-1]; # Quito el bit de paridad
        caracter = chr(int(codigo_ascii, 2)); # Convierto el codigo ASCII a un caracter
        mensaje += caracter;
    return mensaje;








############################ TRABAJO PRACTICO N°5 ################################

def generarMatrizCanal(entrada, salida):
    """
        Entrada es un mensaje que se envia y salida es el mensaje que se recibe
        Se devuelve la matriz del canal

        La entrada y la salida deben tener la misma longitud
    """
    alfabetoEntrada = obtenerAlfabeto(entrada);
    alfabetoSalida = obtenerAlfabeto(salida);

    alfabetoEntrada.sort;
    alfabetoSalida.sort;
    matriz = [];
    for i in alfabetoEntrada:
        fila = [];
        vector_cantidad = [];
        total = 0;
        for simbolo in alfabetoSalida:
            vector_cantidad.append({"simbolo": simbolo, "cantidad": 0});
        for j in range(len(entrada)):
            if i == entrada[j]:
                total += 1;
                for k in vector_cantidad:
                    if k["simbolo"] == salida[j]:
                        k["cantidad"] += 1;
        for k in vector_cantidad:
            fila.append(k["cantidad"] / total);
        matriz.append(fila);
    return matriz;




def probabilidadesSalida(canal, prob_entrada):
    prob_salida = [];
    for j in range(len(canal[0])):
        suma = 0;
        for i in range(len(canal)):
            suma += canal[i][j] * prob_entrada[i];
        prob_salida.append(suma);
    return prob_salida;



def matrizProbabilidadesPosteriori(canal, prob_entrada):
    prob_salida = probabilidadesSalida(canal, prob_entrada);
    matriz_probabilidades_posteriori = [];
    for i in range(len(canal)):
        fila = [];
        for j in range(len(canal[0])):
            if prob_salida[j] == 0:
                fila.append(0);
            else:
                fila.append(canal[i][j] * prob_entrada[i] / prob_salida[j]);
        matriz_probabilidades_posteriori.append(fila);
    return matriz_probabilidades_posteriori;



def matrizSucesosSimultaneos(canal, prob_entrada):
    matriz_sucesos = [];
    prob_salida = probabilidadesSalida(canal, prob_entrada);
    probabilidades_posteriori = matrizProbabilidadesPosteriori(canal, prob_entrada);
    for i in range(len(canal)):
        fila = [];
        for j in range(len(canal[0])):
            fila.append(probabilidades_posteriori[i][j] * prob_salida[j]);
        matriz_sucesos.append(fila);
    return matriz_sucesos;



def entropiasPosteriori(prob_piori, canal):
    matriz_probabilidades_posteriori = matrizProbabilidadesPosteriori(canal, prob_piori);
    entropias = [];
    for j in range(len(canal[0])):
        suma = 0;
        for i in range(len(canal)):
            p = matriz_probabilidades_posteriori[i][j];
            if p != 0:
                suma += p * math.log2(1/p);
        entropias.append(suma);
    return entropias;


def equivocacionCanal(prob_entrada, canal):
    """
        Calcula la equivocacion del canal
        prob_entrada: Probabilidades a priori de la entrada
        canal: Matriz de transicion del canal
    """
    ruido = 0;
    matriz_sucesos = matrizSucesosSimultaneos(canal, prob_entrada);
    probabilidades_posteriori = matrizProbabilidadesPosteriori(canal, prob_entrada);
    for i in range(len(matriz_sucesos)):
        for j in range(len(matriz_sucesos[0])):
            ruido += matriz_sucesos[i][j] * math.log2(1 / probabilidades_posteriori[i][j]) if probabilidades_posteriori[i][j] != 0 else 0;
    return ruido;


def perdidaCanal(prob_entrada, canal):
    """
        Calcula la perdida del canal
        prob_entrada: Probabilidades a priori de la entrada
        canal: Matriz de transicion del canal
    """
    perdida = 0;
    matriz_sucesos = matrizSucesosSimultaneos(canal, prob_entrada);
    for i in range(len(matriz_sucesos)):
        for j in range(len(matriz_sucesos[0])):
            perdida += matriz_sucesos[i][j] * math.log2(1 / canal[i][j]) if canal[i][j] != 0 else 0;
    return perdida;


def entropiaAfin(prob_entrada, canal):
    """
        Calcula la entropia afín del canal
        prob_entrada: Probabilidades a priori de la entrada
        canal: Matriz de transicion del canal
    """
    matriz_sucesos = matrizSucesosSimultaneos(canal, prob_entrada);
    entropia_afin = 0;
    for i in range(len(matriz_sucesos)):
        for j in range(len(matriz_sucesos[0])):
            entropia_afin += matriz_sucesos[i][j] * math.log2(1 / matriz_sucesos[i][j]) if matriz_sucesos[i][j] != 0 else 0;
    return entropia_afin;


def informacionMutua(prob_entrada, canal):
    """
        Calcula la informacion mutua del canal
        prob_entrada: Probabilidades a priori de la entrada
        canal: Matriz de transicion del canal
    """
    matriz_sucesos = matrizSucesosSimultaneos(canal, prob_entrada);
    probabilidades_posteriori = matrizProbabilidadesPosteriori(canal, prob_entrada);
    informacion_mutua = 0;
    for i in range(len(matriz_sucesos)):
        for j in range(len(matriz_sucesos[0])):
            if prob_entrada[i] != 0:
                informacion_mutua += matriz_sucesos[i][j] * math.log2(probabilidades_posteriori[i][j] / prob_entrada[i]) if probabilidades_posteriori[i][j] != 0 else 0;
    return informacion_mutua;
