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




        Explicacion del codigo:
        Calculo r como la longitud del alfabeto del codigo que me dan, despues
        calculo las longitudes de las palabras del codigo que me dan para la extension.
        Con eso calculo la longitud media usando las probabilidades de la extension
        (Sumatoria de cada probabilidad de la extension por la longitud de la palabra correspondiente).
        Calculo la entropia de la fuente original usando las probabilidades de la fuente original y 
        la informacion de la fuente original (calculo la informacion en base r, que es la longitud del alfabeto del codigo).
        Finalmente verifico si se cumple la inecuacion del primer teorema de Shannon


        Conclusion sobre el teorema:
        Este teorema es una forma de acotar la longitud media de un codigo compacto, es decir,
        no se puede comprimir mas alla de la entropia y si el codigo es compacto su longitud media
        no sera mayor a la entropia mas 1

        Este teorema se puede aplicar a la extension de una fuente demostrando que la cantidad de simbolos
        del alfabeto codigo en promedio para un simbolo de la fuente original (Ln / n es ese valor)
        estara entre la entropia de la fuente original y la entropia mas 1/n (En base r)

        Un hecho importante de este teorema es que nos garantiza que la extension de una fuente
        puede tener un codigo que no sea la extension del codigo de la fuente y esto permite que
        a medida que n crece, el codigo sea cada vez mas compacto (La longitud media se acerca a la entropia).
        Sin embargo, el aumento de n tambien aumenta la complejidad del codigo y el tiempo de codificacion/decodificacion

        De esta forma al incrementar n y calcular un codigo para la extension de orden n de la fuente,
        podemos lograr una mayor eficiencia en la codificacion, acercandonos al limite teorico. Ese codigo
        se puede aplicar a cualquier fuente
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

        Explicacion del codigo:
        Calculo r como la longitud del alfabeto del codigo que me dan, despues
        calculo las longitudes de las palabras del codigo que me dan para la extension.
        Con eso calculo la longitud media usando las probabilidades de la extension
        (Sumatoria de cada probabilidad de la extension por la longitud de la palabra correspondiente).
        Calculo la entropia de la fuente original usando las probabilidades de la fuente original y
        la informacion de la fuente original (calculo la informacion en base r, que es la longitud del alfabeto del codigo).
        Finalmente verifico si se cumple la inecuacion del primer teorema de Shannon


        Conclusiones sobre el rendimiento:
        A mayor rendimiento, mas compacto sera el codigo ya que el valor maximo para codigos
        univocos (L >= H) es 1 (L = H). El rendimiento crece cuando la longitud media disminuye
        o cuando la entropia aumenta (Hay mayor informacion en promedio por simbolo)
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

        Conclusiones sobre la redundancia:
        A mayor redundancia, menos compacto sera el codigo ya que la redundancia implica que hay
        simbolos que se repiten innecesariamente, aumentando la longitud del codigo sin aumentar
        la cantidad de informacion transmitida. (L - H). Tambien puede aumentar si baja
        la entropia (Menor cantidad de informacion por simbolo). Si L = H, la redundancia es minima (0) y el rendimiento es maximo (1)
    '''
    return 1 - calcularRendimiento(probabilidades, codigo);



def generarCodigoHuffman(probabilidades):
    """

        Explicacion del codigo:
        Dado un conjunto de probabilidades como:
        S = {s1, s2, s3, s4}
        P = [0.4, 0.3, 0.2, 0.1]

        1. Creo una lista de listas, donde cada sublista contiene la probabilidad y un vector con el indice del simbolo
           Ej: [[0.4, [0]], [0.3, [1]], [0.2, [2]], [0.1, [3]]]
        2. Ordeno la lista de listas en orden descendente por probabilidad
        3. Mientras haya mas de un elemento en la lista:
            a. Saco los dos ultimos elementos de la lista (los de menor probabilidad)
            b. Creo un nuevo elemento con la suma de las probabilidades y la union de los indices
            c. Agrego el nuevo elemento a la lista
            d. Ordeno la lista de listas en orden descendente por probabilidad
            e. A los indices del anteultimo elemento les agrego un 1 al codigo
            f. A los indices del ultimo elemento les agrego un 0 al codigo
        4. Devuelvo el codigo generado
        Por convencion, se agrega un 1 a los elementos del anteultimo y un 0 a los del ultimo
    
    
    """
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
    """
    
        Explicacion del codigo:
        Dado un conjunto de probabilidades como:
        S = {s1, s2, s3, s4}
        P = [0.4, 0.3, 0.2, 0.1]

        1. Creo una lista de listas, donde cada sublista contiene la probabilidad y su indice
              Ej: [[0.4, 0], [0.3, 1], [0.2, 2], [0.1, 3]]
        2. Ordeno la lista de listas en orden descendente por probabilidad
        3. Mientras haya mas de un elemento en la lista:
            a. Calculo la suma total de las probabilidades y la mitad de esa suma
            b. Recorro la lista acumulando las probabilidades hasta que la suma acumulada
               sea mayor o igual a la mitad de la suma total
            c. Divido la lista en dos partes, la primera parte contiene los elementos
               desde el inicio hasta el indice donde se alcanzo la mitad, y la segunda
               parte contiene el resto de los elementos
            d. A los indices de la primera parte les agrego un 1 al codigo
            e. A los indices de la segunda parte les agrego un 0 al codigo
            f. Repito el proceso recursivamente para cada una de las dos partes
        4. Devuelvo el codigo generado
        Por convencion, se agrega un 1 a los elementos de la primera parte y un 0 a los de la segunda parte
    

    """
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

    cantidad_bits_original = len(mensaje_codificado); # Longitud original del mensaje codificado en bits

    # Agrego 0s al final para que la longitud sea multiplo de 8
    n = cantidad_bits_original;
    while n % 8 != 0:
        mensaje_codificado += "0";
        n += 1;
    
    byte_array = bytearray(); # Creo un ByteArray vacio

    # Cargo el primer byte con la cantidad de bits de relleno que agregue
    # Esto es para que al decodificar, sepa cuantos bits debo ignorar al final
    bits_relleno = n - cantidad_bits_original;
    byte_array.append(bits_relleno); # Agrego el byte al ByteArray

    for i in range(0, n, 8): # Recorro de a 8
        byte = mensaje_codificado[i:i+8]; # Tomo 8 bits
        byte_array.append(int(byte, 2)); # Convierto el string de 8 bits a un numero entero en base 2 y lo agrego al ByteArray
    return byte_array


def readFile(name: str) -> bytearray:
    with open(name, 'rb') as file:
        byte_array = bytearray(file.read())
    return byte_array


def decodificarMensaje(mensaje_codificado, fuente, codigo):
    """
        Dado un mensaje codificado en binario (ByteArray), su fuente y un codigo 
        (Codificado en binario), devuelve el mensaje decodificado.

        El byteArray tiene un byte extra al inicio que indica la cantidad de bits de relleno
        que se agregaron al final del mensaje codificado para completar el ultimo byte.

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
    
    # Quito el primer byte que indica la cantidad de bits de relleno
    bits_relleno = int(mensaje_binario[:8], 2);
    mensaje_binario = mensaje_binario[8:]; # Quito el primer byte

    mensaje_decodificado = "";
    i = 0;
    longitud = len(mensaje_binario) - bits_relleno; # Longitud del mensaje sin los bits de relleno
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
    """
        Calcula la tasa en bits y da que tan grande es el mensaje original
        con respecto al mensaje codificado
    """
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
    """
        Explicacion del codigo:
        Dado un codigo (lista de strings de 0s y 1s), calcula la distancia de Hamming
        entre todas las palabras del codigo y devuelve la distancia minima encontrada.

        Pasos:
        1. Inicializo la distancia minima en un valor grande (99999)
        2. Recorro todas las palabras del codigo con dos indices i y j (Comparo cada
           palabra con todas las demas)
        3. Para cada par de palabras (i, j), calculo la distancia de Hamming
           recorriendo los bits de ambas palabras y contando las diferencias
        4. Si la distancia calculada es menor que la distancia minima actual y no es 0,
           actualizo la distancia minima
        5. Devuelvo la distancia minima encontrada

        Conclusiones:
        La distancia de Hamming entre dos palabras cualquiera debe ser mayor o igual
        a la distancia de Hamming del codigo. Eso significa que si entre dos palabras
        hay una distancia menor a la distancia minima del codigo, entonces hay una de
        ellas que tiene un error.
        Si la distancia de hamming es d entonces se pueden detectar d-1 errores
        y se puede corregir (d-1)/2 errores
        Esto es para cualquier mensaje que se envie usando el codigo

        // Por que (d-1)/2?
    """
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
    return (cantidad_1s % 2 == 0 and codigo_binario[-1] != '0') or (cantidad_1s % 2 != 0 and codigo_binario[-1] != '1');



def agregarBitParidadLRC(matriz):
    """
        Recibe una matriz (lista de listas) de bits (0s y 1s)
        Agrega una fila al inicio con los bits de paridad LRC
        Devuelve la matriz con la fila de paridad agregada

        Para usar esta funcion, la matriz debe tener 
        la paridad por palabra ya agregada
    """
    fila_paridad = [];
    for j in range(len(matriz[0])):
        cantidad_1s = 0;
        for i in range(len(matriz)):
            if matriz[i][j] == '1':
                cantidad_1s += 1;
        if cantidad_1s % 2 == 0:
            fila_paridad.append('0'); # Agrego un 0 si la cantidad de 1s es par
        else:
            fila_paridad.append('1'); # Agrego un 1 si la cantidad de 1s es impar
    matriz_con_paridad = [fila_paridad] + matriz; # Agrego la fila de paridad al inicio de la matriz
    return matriz_con_paridad;


def generarSecuenciaBytes(mensaje):
    """

        Dado un mensaje (string), devuelvo un byteArray con la secuencia de bytes
        con el codigo ASCII de cada caracter del mensaje y los bits de paridad
        vertical, longitudinal y cruzada

        Ej:

            ESTE EJEMPLO ES DE LA PRACTICA 9 A MODO DE VER COMO ES EL PROCESO,
            EN ESTE EJERCICIO NO OCURRE ESTO PORQUE EL MENSAJE QUE YO RECIBO
            ES UN STRING Y NO LO ESTOY CODIFICANDO

            Mensaje:            C  A   D  B  C C B  A
            Mensaje Codificado: 0 111 110 10 0 0 10 111

            Quiero transmitir esto por un canal por ejemplo:
            0111110100010111

            Antes de enviarlo por el canal debo agregar los bits de paridad para
            que se pueden detectar los errores

            1) Armo la matriz de bits con bloques de longitud fija
            
                Bits LRC (' ') Bit de paridad cruzada ( () ) y 
                la ultima columna son bits VRC ( " " )

                '1' '1' '0' '0' (0)
                 0   1   1   1  "1"
                 1   1   0   1  "1"
                 0   0   0   1  "1"
                 0   1   1   1  "1"

            2) Vuelvo a armar la secuencia de bits

            '1' '1' '0' '0' (0) 0 1 1 1 "1" 1 1 0 1 "1" 0 0 0 1 "1" 0 1 1 1 "1"

            3) Divido la secuencia en bytes y los envio por el canal

            4) Al recibirlos del canal se podran detectar y corregir errores
    
    """
    matriz = [];
    for caracter in mensaje:
        codigo_ascii = format(ord(caracter), '07b'); # Obtengo el codigo ASCII en binario de 7 bits
        codigo_ascii_con_paridad = agregarBitParidadPalabra(codigo_ascii); # Agrego el bit de paridad
        matriz.append([c for c in codigo_ascii_con_paridad]); # Convierto el string a una lista de caracteres y lo agrego a la matriz

    # En este punto tengo cada caracter del mensaje convertido a su codigo ASCII en binario
    # con su bit de paridad agregado, cada fila de la matriz es una palabra del mensaje

    # Agrego la fila de paridad VRC
    matriz_con_paridad = agregarBitParidadLRC(matriz);

    # Ya tengo la matriz

    # Genero secuencia de bytes
    byte_array = bytearray();
    secuencia_bits = "";
    for fila in matriz_con_paridad:
        for bit in fila:
            secuencia_bits += str(bit);
    n = len(secuencia_bits);

    # Agrego 0s al final para que la longitud sea multiplo de 8
    while n % 8 != 0:
        secuencia_bits += "0";
        n += 1;
    for i in range(0, n, 8): # Recorro de a 8
        byte = secuencia_bits[i:i+8]; # Tomo 8 bits
        byte_array.append(int(byte, 2)); # Convierto el string de 8 bits a un numero entero en base 2 y lo agrego al ByteArray
    return byte_array;



def obtenerMensajeOriginal(byte_array):
    """
    
        Dado un byteArray con la secuencia de bytes recibida, obtengo el mensaje original
        Cada byte es un entero en base 2 que representa 8 bits (7 bits del caracter y 
        1 bit de paridad)

        ESTA FUNCION SE ENCARGA DE OBTENER EL MENSAJE QUE SE ENVIO CON LA FUNCION
        "generarSecuenciaBytes"

    """
    secuencia_bits = "";
    for byte in byte_array:
        secuencia_bits += format(byte, '08b'); # Convierto cada byte a un string de 8 bits y lo agrego al string

    # Quito los bits de relleno al final
    # Primero obtengo la cantidad de columnas (longitud de una fila)
    cantidad_columnas = 8; # En este caso es 8 porque cada fila tiene 8 bits (7 bits + 1 bit de paridad)
    cantidad_filas = len(secuencia_bits) // cantidad_columnas;

    # Quito los bits de relleno al final
    total_bits = cantidad_filas * cantidad_columnas;
    secuencia_bits = secuencia_bits[:total_bits];

    # Rearmo la matriz
    matriz = [];
    for i in range(cantidad_filas):
        fila = [];
        for j in range(cantidad_columnas):
            fila.append(int(secuencia_bits[i * cantidad_columnas + j]));
        matriz.append(fila);

    # Quito la fila de paridad VRC
    matriz_sin_paridad = matriz[1:];

    # Quito el bit de paridad de cada palabra y obtengo el mensaje original
    mensaje_original = "";
    for fila in matriz_sin_paridad:
        codigo_ascii_con_paridad = ''.join([str(bit) for bit in fila]); # Convierto la lista de enteros a un string
        codigo_ascii = codigo_ascii_con_paridad[:-1]; # Quito el bit de paridad
        caracter = chr(int(codigo_ascii, 2)); # Convierto el codigo ASCII a un caracter
        mensaje_original += caracter;
    return mensaje_original;



# Funciones que agrego yo para utilidad
def generarMatrizParidad(mensaje):
    """

        Dado un mensaje (string), genero la matriz de paridad

    """
    matriz = [];
    for caracter in mensaje:
        codigo_ascii = format(ord(caracter), '07b'); # Obtengo el codigo ASCII en binario de 7 bits
        codigo_ascii_con_paridad = agregarBitParidadPalabra(codigo_ascii); # Agrego el bit de paridad
        matriz.append([c for c in codigo_ascii_con_paridad]); # Convierto el string a una lista de caracteres y lo agrego a la matriz

    # En este punto tengo cada caracter del mensaje convertido a su codigo ASCII en binario
    # con su bit de paridad agregado, cada fila de la matriz es una palabra del mensaje

    # Agrego la fila de paridad VRC
    matriz_con_paridad = agregarBitParidadLRC(matriz);
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


# NO FUNCIONA DEL TODO BIEN
def matrizTieneErrores(matriz):
    """

        Dada una matriz de paridad, verifica si tiene errores

    """
    # Verifico la fila de paridad VRC
    fila_paridad = matriz[0];
    for j in range(len(fila_paridad)):
        cantidad_1s = 0;
        for i in range(1, len(matriz)):
            if matriz[i][j] == '1':
                cantidad_1s += 1;
        if cantidad_1s % 2 == 0 and fila_paridad[j] != '0':
            return True; # Tiene error
        if cantidad_1s % 2 != 0 and fila_paridad[j] != '1':
            return True; # Tiene error

    # Verifico los bits de paridad de cada palabra
    for i in range(1, len(matriz)):
        fila = matriz[i];
        cantidad_1s = fila.count('1');
        if cantidad_1s % 2 == 0 and fila[-1] != '0':
            return True; # Tiene error
        if cantidad_1s % 2 != 0 and fila[-1] != '1':
            return True; # Tiene error

    return False; # No tiene errores


# Pruebas de las funciones
#mensaje = "Enzo"
#matriz_paridad = generarMatrizParidad(mensaje)
#mensaje_recuperado = mensajeMatrizParidad(matriz_paridad)
#print("Matriz de paridad: ")
#for fila in matriz_paridad:
    #print(fila)
#print("Mensaje original: ", mensaje)
#print("Mensaje recuperado: ", mensaje_recuperado)

#byte_array = generarSecuenciaBytes(mensaje)
#mensaje_recibido = obtenerMensajeOriginal(byte_array)
#print("Secuencia de bytes: ", list(byte_array))
#print("Mensaje recibido: ", mensaje_recibido)







############################ TRABAJO PRACTICO N°5 ################################

def generarMatrizCanal(entrada, salida):
    """
        Entrada es un mensaje que se envia y salida es el mensaje que se recibe
        Se devuelve la matriz del canal

        La entrada y la salida deben tener la misma longitud

        Explicacion del codigo:
        1. Obtengo el alfabeto de la entrada y el alfabeto de la salida
        2. Recorro cada simbolo del alfabeto de la entrada
        3. Para cada simbolo de la entrada, recorro cada simbolo del alfabeto de la salida
        4. Cuento la cantidad de veces que el simbolo de la entrada se mapea al simbolo de la salida
        5. Divido la cantidad de veces que el simbolo de la entrada se mapea al simbolo de la salida
           por la cantidad total de veces que aparece el simbolo de la entrada
        6. Agrego la fila a la matriz del canal
        7. Devuelvo la matriz del canal

        Las filas deben sumar 1 ya que dado que entre un valor, tengo que salir por algun valor
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
    """

        Calcula las probabilidades de salida del canal
        canal: Matriz de transicion del canal
        prob_entrada: Probabilidades a priori de la entrada

        Explicacion del codigo:
        1. Inicializo una lista vacia para las probabilidades de salida
        2. Recorro cada columna de la matriz del canal
        3. Para cada columna, recorro cada fila de la matriz del canal
        4. Multiplico la probabilidad de entrada por la probabilidad condicional
           y la sumo a la probabilidad de salida correspondiente
        5. Agrego la probabilidad de salida a la lista de probabilidades de salida
        6. Devuelvo la lista de probabilidades de salida

    """
    prob_salida = [];
    for j in range(len(canal[0])):
        suma = 0;
        for i in range(len(canal)):
            suma += canal[i][j] * prob_entrada[i];
        prob_salida.append(suma);
    return prob_salida;



def matrizProbabilidadesPosteriori(canal, prob_entrada):
    """
    
        Calcula la matriz de probabilidades a posteriori
        canal: Matriz de transicion del canal
        prob_entrada: Probabilidades a priori de la entrada

        Explicacion del codigo:
        1. Calculo las probabilidades de salida del canal
        2. Inicializo una lista vacia para la matriz de probabilidades a posteriori
        3. Recorro cada fila de la matriz del canal
        4. Para cada fila, recorro cada columna de la matriz del canal
        5. Calculo la probabilidad a posteriori usando la formula de Bayes (Esto es 
           P(bj / ai) * P(ai) / P(bj))
        6. Agrego la probabilidad a posteriori a la fila
        7. Agrego la fila a la matriz de probabilidades a posteriori
        8. Devuelvo la matriz de probabilidades a posteriori

    """
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
    """

        Calcula la matriz de sucesos simultaneos
        canal: Matriz de transicion del canal
        prob_entrada: Probabilidades a priori de la entrada

        Explicacion del codigo:
        1. Calculo las probabilidades de salida del canal
        2. Calculo la matriz de probabilidades a posteriori
        3. Inicializo una lista vacia para la matriz de sucesos simultaneos
        4. Recorro cada fila de la matriz del canal
        5. Para cada fila, recorro cada columna de la matriz del canal
        6. Calculo el suceso simultaneo multiplicando la probabilidad a posteriori
           por la probabilidad de salida
        7. Agrego el suceso simultaneo a la fila
        8. Agrego la fila a la matriz de sucesos simultaneos
        9. Devuelvo la matriz de sucesos simultaneos

        Conclusiones:
        En un buen canal la diagonal principal de la matriz de sucesos simultaneos
        deberia tener los valores mas altos, ya que eso indica que la probabilidad
        de que la salida sea igual a la entrada es alta. Y la diagonal secundaria
        deberia tener valores bajos, ya que eso indica que la probabilidad de que
        la salida sea distinta a la entrada es baja.

    """
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
    """
    
        Calcula las entropias a posteriori del canal
        prob_piori: Probabilidades a priori de la entrada
        canal: Matriz de transicion del canal

        Explicacion del codigo:
        1. Calculo la matriz de probabilidades a posteriori
        2. Inicializo una lista vacia para las entropias
        3. Recorro cada columna de la matriz del canal
        4. Para cada columna, recorro cada fila de la matriz del canaL
        5. Multiplico la probabilidad a posteriori por el logaritmo en base 2 de su inverso
        6. Sumo los valores obtenidos para cada fila y los agrego a la lista de entropias
        7. Devuelvo la lista de entropias


        Conclusiones:

        1) La entropia a priori nos dice la incertidumbre media para los simbolos
        de entrada del canal, mientras que la entropia a posteriori dice
        la incertidumbre media de los simbolos de entrada dado que ocurra
        tal simbolo de salida.

        2) Es la incertidumbre que queda sobre la entrada al conocer la salida.

        Para sacar conclusiones sobre los valores no hay una regla general,
        dependo del canal y las probabilidades de entrada.

        3) Si mi canal es perfecto, la entropia a posteriori sera 0 para todas las salidas
        ya que al conocer la salida conozco la entrada con certeza.

        4) Si mi canal es ruidoso, la entropia a posteriori sera mayor a 0 para todas las salidas
        ya que al conocer la salida no conozco la entrada con certeza.



        Estas se cumplen?????????
        5) La entropia a posteriori sera mas grande para las salidas mas probables

        6) Si la entropia a priori es maxima (Probabilidades de entrada equiprobables), 
        la entropia a posteriori sera menor o igual a la entropia a priori.
        Disminuye menos para la salida mas probable y mas para las demas salidas.
    
    """
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
        Devuelve la equivocacion del canal (H(A/B))

        Explicacion del codigo:
        La equivocacion del canal se puede obtener como el promedio
        de las entropias a posteriori, sumo cada entropia multiplicada
        por la probabilidad de salida correspondiente.

        La otra forma de obtenerla es usando la matriz de sucesos simultaneos
        y la matriz de probabilidades a posteriori, sumando cada suceso
        simultaneo multiplicado por el logaritmo en base 2 de la inversa
        de la probabilidad a posteriori correspondiente.


        Conclusiones:
        1) Mide la informacion que queda en A despues de conocer B
        2) Perdida de informacion sobre A causada por el canal
        3) Cantidad de informacion sobre A que no deja pasar el canal
        4) Numero minimo de preguntas binarias en promedio para determinar la entrada
           conocida la salida
        5) NOTA: Es el primedio de las incertidumbres sobre A para cada salida B
        
        A las salidas que son producto del canal y no corresponden a entradas se
        las agrupa como b = *, si H(A/b = *) > H(A) entonces hay mas incertidumbre
        al conocer la salida que sin conocerla

        Una ley universal es que H(A/B) <= H(A). En promedio
        nunca puede suceder que al conocer B la incertidumbre sobre A aumente.
        A pesar de que para algunas salidas particulares la incertidumbre sobre A
        pueda aumentar (Eso ocurre con los b = *, salidas que no corresponden
        a ninguna entrada)

        
        Ej:
        
        A es "¿Lloverá hoy?" y B es "El pronóstico del tiempo."

        Antes de ver el pronóstico (H(A)): Hay cierta incertidumbre sobre si lloverá o no.

        Después de ver el pronóstico (H(A|B)): La incertidumbre sobre si lloverá debería disminuir.

        En el peor caso, si el pronóstico es inútil (no tiene relación con el clima real), 
        la incertidumbre se mantiene igual. 
        Pero nunca puede suceder que, en promedio, saber el pronóstico haga 
        aumentar la incertidumbre sobre si lloverá. 

    """

    # Equivalencia usando matriz de sucesos simultaneos
    ruido = 0;
    matriz_sucesos = matrizSucesosSimultaneos(canal, prob_entrada);
    probabilidades_posteriori = matrizProbabilidadesPosteriori(canal, prob_entrada);
    for i in range(len(matriz_sucesos)):
        for j in range(len(matriz_sucesos[0])):
            ruido += matriz_sucesos[i][j] * math.log2(1 / probabilidades_posteriori[i][j]) if probabilidades_posteriori[i][j] != 0 else 0;

    # Equivalencia usando entropias a posteriori
    #entropias_posteriori = entropiasPosteriori(prob_entrada, canal);
    #prob_salida = probabilidadesSalida(canal, prob_entrada);
    #for j in range(len(entropias_posteriori)):
        #ruido += prob_salida[j] * entropias_posteriori[j];
    return ruido;


def perdidaCanal(prob_entrada, canal):
    """
        Calcula la perdida del canal
        prob_entrada: Probabilidades a priori de la entrada
        canal: Matriz de transicion del canal
        Devuelve la perdida del canal (H(B/A))

        Explicacion del codigo:
        La perdida del canal se puede obtener usando la matriz de sucesos simultaneos
        sumando cada suceso simultaneo multiplicado por el logaritmo en base 2 
        de la inversa de la probabilidad condicional correspondiente (Como esa es P(b/a)
        la obtengo directamente de la matriz del canal  )

        Conclusiones:
        1) Mide la informacion que no llega a B desde A
        2) Es la incertidumbre que hay sobre la salida al conocer la entrada
        3) Mide la incertidumbre promedio sobre la salida dado que se envio A
        4) Es una medida de la corrupcion del canal, que tanto se distorsiona la entrada
           al pasar por el canal

        Numero minimo de preguntas binarias en promedio para determinar la salida
        conocida la entrada 

    """
    # Otra forma de calcularla es: Sumatoria de P(Ai).H(B/Ai), es decir,
    # sumo las entropias condicionales de la salida dado cada entrada multiplicadas
    # por la probabilidad de la entrada correspondiente
    # La entropia condicional no tiene interpretacion, solo es una forma de
    # calcularla 

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
        Devuelve la entropia afín del canal (H(A, B))

        Explicacion del codigo:
        La entropia afín se puede obtener usando la matriz de sucesos simultaneos
        sumando cada suceso simultaneo multiplicado por el logaritmo en base 2 
        de su inversa.

        Conclusiones:
        Es una medida de la incertidumbre del suceso simultaneo (ai, bj)
        Su valor coincide con H(B) + H(A/B) y con H(A) + H(B/A)

        H(A) es el numero de binits necesarios para definir la entrada
        H(B) es el numero de binits necesarios para definir la salida
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

        Explicacion del codigo:
        Se puede obtener como H(A) - H(A/B) (Esto es calcular por relacion)
        o usando la matriz de sucesos simultaneos y la matriz de probabilidades a posteriori.
        (Esto es calcular por definicion). 

        Otra forma de hacerlo por definicion es
        hacer la sumatoria de P(ai, bj) * log2( P(ai, bj) / (P(ai) * P(bj)) )

        Con esto veo claramente que se cumple la reciprocidad de la informacion mutua
        I(A, B) = I(B, A)

        ############################ CONSULTAR ############################
        ¿Como hago I(B, A)??????????????????
        Para calcularlo es lo mismo pero invirtiendo el orden de las variables
        (P(B,A) * log( P(B,A) / (P(B) * P(A)) ) )


        1. Calculo la matriz de sucesos simultaneos
        2. Calculo la matriz de probabilidades a posteriori
        3. Inicializo la variable de informacion mutua en 0
        4. Recorro cada fila de la matriz de sucesos simultaneos
        5. Para cada fila, recorro cada columna de la matriz de sucesos simultaneos
        6. Sumo a la variable de informacion mutua la probabilidad del suceso simultaneo
           multiplicado por el logaritmo en base 2 de la probabilidad a posteriori dividido 
           por la probabilidad de entrada
        7. Devuelvo la variable de informacion mutua


        Conclusiones:
        Yo tengo incertidumbre sobre la entrada A.  
        La información mutua me dice cuánta de esa incertidumbre perdí
        después de pasar A por el canal y conocer la salida B.
        Es decir, al conocer B, cuánta incertidumbre sobre A se resuelve
        y por ende cuánta información sobre A realmente pasó a través del canal.

        La información mutua es un índice que indica qué tan bien se está 
        aprovechando un canal para transmitir información. Este valor depende 
        tanto del canal como de la distribución de la fuente que genera 
        los símbolos de entrada.

        La información mutua depende no solamente del arreglo de
        probabilidades condicionales relacionadas al canal de entrada y
        salida, sino también de las probabilidades con las cuales los
        diversos canales de símbolos de entrada son escogidos.

        Propiedades:
        a) No se pierde en absoluto información por el hecho de observar la salida del canal. 
        Además la condición para que la información mutua sea nula es que los 
        símbolos de entrada y salida sea estadisticamente independientes.
        
        b) I (A,B) es simétrica respecto a las variables ai y bj. 
        Por lo tanto, podrá escribirse:
            I (A,B) = I (B, A) (reciprocidad de la información mutua).
        
        c) Luego:
            I (A,B) = H (B) - H (B/A)
            H(A,B)=H(A)+H(B)-I(A,B)
        
    """
    matriz_sucesos = matrizSucesosSimultaneos(canal, prob_entrada);
    probabilidades_posteriori = matrizProbabilidadesPosteriori(canal, prob_entrada);
    informacion_mutua = 0;
    for i in range(len(matriz_sucesos)):
        for j in range(len(matriz_sucesos[0])):
            if prob_entrada[i] != 0:
                informacion_mutua += matriz_sucesos[i][j] * math.log2(probabilidades_posteriori[i][j] / prob_entrada[i]) if probabilidades_posteriori[i][j] != 0 else 0;
    return informacion_mutua;






##################### TRABAJO PRACTICO N°6 ######################


def esCanalSinRuido(canal):
    """

        Explicacion del codigo:
        1. Recorro cada columna de la matriz del canal
        2. Para cada columna, recorro cada fila de la matriz del canal
        3. Cuento la cantidad de valores distintos de cero en la columna
        4. Si la cantidad de valores distintos de cero es distinta de 1,
           entonces el canal tiene ruido y devuelvo False
        5. Si recorro toda la matriz y en cada columna hay un solo valor
              distinto de cero, entonces el canal no tiene ruido y devuelvo True

        Conclusiones:
        Al observarse una salida se sane con certeza cual fue la entrada que la produjo. (Pero
        al reves no ya que una entrada puede producir varias salidas distintas)
        La equivocacion es 0 ya que no hay incertidumbre sobre la entrada al conocer la salida.
        (El numero de binits necesarios para definir la entrada al conocer la salida es 0, 
        la entropia a posteriori es 0 para todas las salidas).
        La informacion mutua es maxima y coincide con la entropia de la entrada.
        Esto ultimo quiere decir que toda la informacion de la entrada pasa por el canal
        sin perderse nada y se resolvio toda la incertidumbre sobre la entrada al conocer la salida.
              
    """
    cumple = True;
    j = 0;
    while(j < len(canal[0]) and cumple):
        i = 0;
        contador_distintos_cero = 0;
        while(i < len(canal) and cumple):
            if canal[i][j] != 0:
                contador_distintos_cero += 1;
            i += 1;
        if contador_distintos_cero != 1:
            cumple = False;
        j += 1;
    return cumple;


def esCanalDeterminante(canal):
    """
    
        Explicacion del codigo:
        1. Recorro cada fila de la matriz del canal
        2. Para cada fila, recorro cada columna de la matriz del canal
        3. Cuento la cantidad de valores distintos de cero en la fila
        4. Si la cantidad de valores distintos de cero es distinta de 1,
            entonces el canal no es determinante y devuelvo False
        5. Si recorro toda la matriz y en cada fila hay un solo valor
            distinto de cero, entonces el canal es determinante y devuelvo True
        
        Conclusiones:
        Al observarse una entrada se sabe con certeza cual será la salida producida. (Pero
        al reves no ya que una salida puede ser producida por varias entradas distintas)
        La perdida es 0 ya que no hay incertidumbre sobre la salida al conocer la entrada,
        I(A,B) = H(B) ya que toda la informacion de la salida se obtiene al conocer la entrada.
    
    """
    cumple = True;
    i = 0;
    while(i < len(canal) and cumple):
        j = 0;
        contador_distintos_cero = 0;
        while(j < len(canal[0]) and cumple):
            if canal[i][j] != 0:
                contador_distintos_cero += 1;
            j += 1;
        if contador_distintos_cero != 1:
            cumple = False;
        i += 1;
    return cumple;





def generarMatrizCompuestaSerie(canal1, canal2):
    """
        canal1: Matriz de transicion del primer canal
        canal2: Matriz de transicion del segundo canal

        La forma correcta es multiplicar canal1 x canal2
        y el resultado será la matriz del canal compuesto.

        Explicacion del codigo:
        Para multiplicar dos matrices, se recorre cada fila de la primera matriz y, para 
        cada una de ellas, se recorre cada columna de la segunda matriz.
        En cada combinación fila–columna se calcula una sumatoria, multiplicando los 
        elementos correspondientes de la fila de la primera matriz por los elementos de 
        la columna de la segunda.
        Esa sumatoria representa el valor del elemento resultante en esa posición y se 
        coloca en la matriz nueva.
        Al repetir este proceso para todas las filas y columnas, se obtiene la matriz 
        producto.
        Finalmente se devuelve la nueva matriz compuesta.



        Conclusiones:
        Cada elemento de la matriz representa la probabilidad de que ocurra Ci
        dado que ocurrio Bj, Ai. Es decir, dado que Ai y Bj ocurrieron en simultaneo
        (P(Ci / Bj, Ai) = P(Ci / Bj)).
        La probabilidad de que ocurra Ai dado que ocurrio Bj es igual a la probabilidad
        de que ocurra Bj y Ck simultaneamente (P(Ai/Bj,Ck) = P(Ai, Bj))

        La equivocacion aumenta (H(A/C) >= H(A/B)) ya que al agregar un canal
        intermedio entre la entrada y la salida, se agrega incertidumbre sobre
        la entrada al conocer la salida. A medida que agrego canales intermedios,
        la equivocacion aumenta.

        I(A,B) >= I(A,C) ya que al agregar un canal intermedio entre
        la entrada y la salida, se pierde informacion sobre la entrada al conocer la salida.
        (La informacion que logro pasar de A a B no llegara toda a C, por eso la relacion)
 
    """

    matriz_compuesta = []
    for i in range(len(canal1)):                      # Filas de canal1
        fila = []
        for j in range(len(canal2[0])):               # Columnas de canal2
            suma = 0
            for k in range(len(canal2)):              # Filas de canal2 (== columnas de canal1)
                suma += canal1[i][k] * canal2[k][j]
            fila.append(suma)
        matriz_compuesta.append(fila)

    return matriz_compuesta


def esReduccionSuficiente(canal, j1, j2):
    """
        Dado dos columnas j1 y j2 de la matriz del canal,
        verifica si las columnas se pueden combinar en una
        reduccion suficiente.

        Canal Reducido:
        Dado un canal, se reduce la matriz de forma "inventada", el canal sigue siendo
        el mismo. Pero se reduce la matriz para facilitar el analisis.
        Este proceso de reduccion se puede hacer muchas veces (Hasta llegar llegar)
        a la reduccion elemental del mismo, P).

        La reduccion de un canal disminuye o a lo sumo mantiene constante la 
        informacion mutua del canal.
        ¿Cuando la mantiene constante?
        Esto ocurre cuando hay una reduccion suficiente entre dos columnas del canal
        que se quiere reducir, desde el punto de vista de la informacion, 
        P(a/b1) = P(a/b2) para toda entrada del canal. Si yo combino las columnas
        obtengo un canal equivalente desde el punto de vista de la informacion (No
        pierdo informacion)

        La reduccion es posible gracias a que un canal se puede extender



        Con la conclusion de que para reducir un canal se debe encontrar dos columnas
        que P(a/b1) = P(a/b2) para toda a, surge la Reduccion Suficiente

        Si la matriz del canal cumple para dos columnas cualquiera:
            P( b1 /a)=const × P (b 2/ a) para cualquier a
        
        Entonces el canal se puede reducir, logrando que no importe las probabilidades
        a piori, no habra perdida de informacion y las informaciones mutuas seran identicas.

        Una vez que se detectecta que un canal es reduccion suficiente se puede hacer:
        
        Una forma de lograr la reduccion matematicamente es agregar un canal
        determinante en serie a un canal, de esa forma, el canal compuesto
        sera una reduccion del canal original

        En el proceso de reduccion, las entradas se mantienen fijas pero cada
        canal reducido tendra su propio alfabeto de salida


        NOTA: Yo puedo reducir lo que quiera, pero en algun momento habra perdida
        de informacion, ahi debo frenar de reducir (Cuando ya no es reduccion suficiente)



        Explicacion del codigo:
        Este codigo se encarga de ver si se cumple la propiedad de Reduccion Suficiente,
        para eso 



    """
    constantes = [];
    for i in range(len(canal)):
        if canal[i][j2] == 0:
            if canal[i][j1] != 0:
                return False;
        else:
            constantes.append(canal[i][j1] / canal[i][j2]);
    primera_constante = constantes[0];
    for c in constantes:
        if c != primera_constante:
            return False;
    return True;



def identidad(n):
    matriz = [[0] * n for _ in range(n)]
    for i in range(n):
        matriz[i][i]=1
    return matriz


# Por que funciona esto?
def matrizDeterminanteParaReducir(canal, j1, j2):
    """

        Explicacion del codigo:
        1. Genero una matriz identidad de tamaño n x n, siendo n la cantidad
            de columnas de la matriz del canal
        2. Sumo la columna j2 a la columna j1
        3. Elimino la columna j2 de la matriz
        4. Devuelvo la matriz resultante

        Conclusiones:
        Al sumar la columna j2 a la columna j1, estoy haciendo que
        el 1 de la posicion [j2][j2] termine en la posicion [j2][j1],
        esto hace que al eliminar la columna j2, la informacion de
        la columna j2 se mantenga en la columna j1.

    """
    matrizDet = identidad(len(canal[0]))

    # Sumar columna2 a columna1
    # Entonces el 1 de la posicion [columna2][columna2] termina en la posicion [columna2][columna1]
    matrizDet[j2][j1] = matrizDet[j2][j2]

    # Eliminar la columna columna2 (ya fue combinada) y me queda una matriz con n columnas (El total de columnas de matriz)
    # y de n-1 columnas (Columnas de matriz)
    for fila in matrizDet:
        fila.pop(j2)

    return matrizDet


def canalEsReducible(canal):
    """
    
        Dada la matriz de un canal, verifica si el canal es reducible
        aplicando reducciones suficientes.

        Devuelve j1 y j2 las columnas que se pueden reducir
        o -1 y -1 si no se pueden reducir
    
    """
    hay_columnas_para_reducir = False;
    j = 0;
    while j < len(canal[0]) and not hay_columnas_para_reducir:
        k = j + 1;
        while k < len(canal[0]) and not hay_columnas_para_reducir:
            if esReduccionSuficiente(canal, j, k):
                hay_columnas_para_reducir = True;
            k += 1;
        j += 1;
    if not hay_columnas_para_reducir:
        return -1, -1;
    else:
        return j - 1, k - 1;



def reducirCanal(canal):
    """
        Dada la matriz de un canal, reduce el canal
        aplicando reducciones suficientes hasta que no
        se puedan aplicar mas.

        Explicacion del codigo:
        1. Recorro cada par de columnas de la matriz del canal
        2. Para cada par de columnas, verifico si se cumple la
           propiedad de reduccion suficiente
        3. Si se cumple la propiedad, genero la matriz determinante
           para reducir el canal    
        4. Genero la matriz reducida aplicando la matriz determinante
        5. Llamo recursivamente a la funcion reducirCanal con la
           matriz reducida
        6. Si no se encuentran mas columnas para reducir, devuelvo
           la matriz del canal actual
        7. Devuelvo la matriz reducida

    """
    j1, j2 = canalEsReducible(canal);
    if j1 == -1 and j2 == -1:
        return canal;
    else:
        matriz_determinante = matrizDeterminanteParaReducir(canal, j1, j2);
        matriz_reducida = generarMatrizCompuestaSerie(canal, matriz_determinante);
        return reducirCanal(matriz_reducida);


def esCanalUniforme(canal):
    """
        Verifica si un canal es uniforme.
        Un canal es uniforme si todas las filas de su matriz son iguales.

        "Explicacion del codigo:
        1. Obtengo la primera fila de la matriz del canal
        2. Recorro cada fila de la matriz del canal
        3. Para cada fila, recorro cada columna de la matriz del canal
    

        Conclusiones:
        Que sea uniforme implica que todas las filas son permutaciones entre si.
        Pero que todas las filas sean permutaciones entre si no implica que sea uniforme.

    """
    primera_fila = canal[0];
    es_uniforme = True;
    i = 0;
    while es_uniforme and i < len(canal):
        j = 0;
        while es_uniforme and j < len(canal[0]):
            if not(canal[i][j] in primera_fila):
                es_uniforme = False;
            j += 1
        i += 1;
    return es_uniforme;


def esCanalSimetrico(canal):
    """

        Es un tipo de canal uniforme en el que no solo todas las filas son permutaciones
        entre si, sino que tambien todas las columnas son permutaciones entre si.

        Explicacion del codigo:
        1. Recorro cada fila de la matriz del canal
        2. Para cada fila, obtengo la fila ordenada
        3. Obtengo la columna correspondiente ordenada
        4. Comparo la fila ordenada con la columna ordenada
        5. Si son distintas, el canal no es simetrico y devuelvo False
        6. Si recorro toda la matriz y todas las filas ordenadas son iguales
            a sus columnas ordenadas, entonces el canal es simetrico y devuelvo True
        


    """
    es_simetrico = True;
    i = 0;
    while es_simetrico and i < len(canal):
        fila = sorted(canal[i]);
        columna = sorted([canal[j][i] for j in range(len(canal))]);
        if fila != columna:
            es_simetrico = False;
        i += 1;
    return es_simetrico;


def capacidadCanalDeterminante(canal):
    """

        Se puede calcular asi porque al ser un canal determinante
        porque I(A,B) = H(B) - H(B/A) y H(B/A) = 0 

    """
    n_salidas = len(canal[0]);
    return math.log2(n_salidas);


def capacidadCanalSinRuido(canal):
    """
    
        Se puede calcular asi porque al ser un canal sin ruido
        porque I(A,B) = H(A) - H(A/B) y H(A/B) = 0

    """
    n_entradas = len(canal);
    return math.log2(n_entradas);



def capacidadCanalUniforme(canal):
    """
    
        Explicacion del codigo:
        1. Calculo la cantidad de salidas del canal
        2. Inicializo una variable suma en 0
        3. Recorro cada columna de la matriz del canal
        4. Para cada columna, sumo a la variable suma el valor de la columna
           multiplicado por el logaritmo en base 2 de su inverso
        5. Devuelvo el logaritmo en base 2 de la cantidad de salidas menos la suma

        Conclusiones:
        Al ser un canal uniforme, todas las filas son iguales pero permutadas.
        Por lo tanto, H(A/B) es igual para todas las entradas del canal.
        Entonces, para calcular la capacidad del canal, se puede usar
        C = log2(n_salidas) - H(A/B)

    """
    n_salidas = len(canal[0]);
    sum = 0;
    for j in range(len(canal[0])):
        sum += canal[0][j] * math.log2(1 / canal[0][j]) if canal[0][j] != 0 else 0;
    return math.log2(n_salidas) - sum;


def capacidadCanalSimetrico(canal):
    """

        Se puede calcular asi porque al ser un canal simetrico
        porque todas las filas y columnas son iguales pero permutados.
        Un simetrico puede ser uniforme, pero no al reves
        Se calcula el log2(n_entradas) - H(A/B) siendo H(A/B)
    
    """
    n_entradas = len(canal);
    sum = 0;
    for j in range(len(canal[0])):
        for i in range(n_entradas):
            sum += canal[i][j] * math.log2(1 / canal[i][j]) if canal[i][j] != 0 else 0;
    return math.log2(n_entradas) - sum;



def capacidadCanal(canal):
    """

        Calcula la capacidad del canal segun su tipo
        canal: Matriz de transicion del canal

        La capacidad de un canal es la máxima tasa a la que se puede transmitir 
        información de manera confiable a través de ese canal.

        Es el límite teórico máximo de bits por segundo que puedes enviar con probabilidad 
        de error arbitrariamente cercana a cero

        No es la velocidad de transmisión física, sino el límite fundamental impuesto 
        por el ruido y las características del canal

        C = max P(a) I(A,B)
        La capacidad se calcula como la máxima información mutua entre la entrada y la salida,
        esta se obtiene variando las probabilidades a priori de la entrada.
        Se debe encontrar una probabilidad de entrada que maximice la informacion mutua.

        Para lograrlo se debe hacer:
        ∂(I A,B)) 
        -------- =0 → p es óptima
        ∂p 

        Si el numero de entradas es igual a 2 se obtiene derivando I(A,B) respecto a p
        y si es > 2 se debe calcular derivadas parciales respecto de las diferentes
        probabilidades de entrada o usando metodos numericos

        Para ciertos canales se calcula de un modo especial
        

        Conclusion:
        Si intentas transmitir datos a una velocidad mayor que 
        C, es matemáticamente imposible reconstruir el mensaje sin errores. 
        Si transmites por debajo de C, Shannon demostró que siempre 
        existe un código lo suficientemente inteligente para corregir casi todos 
        los errores.

        Es el máximo acople posible entre la entrada y la salida
        Es la maxima cantidad de informacion que puede transmitir el canal
        

    """
    if(esCanalDeterminante(canal)):
        print("Es canal determinante");
        return capacidadCanalDeterminante(canal);
    else:
        if (esCanalSimetrico(canal)):
            print("Es canal simetrico");
            return capacidadCanalSimetrico(canal);
        else:
            if (esCanalUniforme(canal)):
                print("Es canal uniforme");
                return capacidadCanalUniforme(canal);
            else:
                if (esCanalSinRuido(canal)):
                    print("Es canal sin ruido");
                    return capacidadCanalSinRuido(canal);
                else:
                    return None; # TODO implementar capacidad general



def capacidadEstimadaBSC(matriz, p):
    """
        Calcula la capacidad de un canal binario
        matriz: Matriz de transicion del canal
        p: Paso para variar las probabilidades de entrada

        Como el BSC es un canal simetrico la capacidad: 1 - H2(P) (Entropia en base 2)
        P es la probabilidad de entrada de algun simbolo (Seria el w) y la del otro
        simbolo es 1 - P

        Si tuviera P se calcula como: 
        H(P)= Not(P) * log (1/ Not(P)) + P log 1/P




        Puede ser que no me den P y me den un valor de paso (Esto es el incremento
        para variar las probabilidades de entrada) para hacer una busqueda por fuerza bruta
        y encontrar la capacidad del canal binario.
        Yo voy variando la distribucion de probabilidades para maximizar la informacion mutua
        y quedandome con el valor maximo que obtenga.

        Con esto metodo hago una ESTIMACION de la capacidad



        
        Version Tino
    
        p funciona como el paso para variar las probabilidades de entrada
        Solo funciona para canales binarios
        Yo no conozco una forma analitica de calcular la capacidad de un canal generico
        por lo que hago una busqueda por fuerza bruta variando las probabilidades de entrada
        y quedandome con el par que mayor informacion mutua me de




        Explicacion del codigo:
        1. Inicializo la variable capacidad en -1
        2. Inicializo las probabilidades de entrada p1 en 1 y p2 en 0
        3. Mientras p2 sea menor a 1, hago:
            a. Calculo la informacion mutua con las probabilidades [p1, p2]
            b. Si la informacion mutua es mayor a la capacidad actual, hago:
                i. Actualizo la capacidad con la informacion mutua
                ii. Actualizo las probabilidades asociadas con [p1, p2]
            c. Resto p al valor de p1
            d. Sumo p al valor de p2
        4. Devuelvo la capacidad y las probabilidades asociadas



        Conclusiones:
        Mientras mas bajo sea el paso mas aproximada seran las probabilidades 
        a las reales
    
    """
    capacidad = -1
    p1 = 1
    p2 = 0
    probs_asociada = []
    while (p2<1):
        info_mutua = informacionMutua([p1, p2], matriz)
        if (info_mutua>capacidad):
            capacidad = info_mutua
            probs_asociada = [round(p1,5), round(p2,5)]
        p1 -= p
        p2 += p
    return round(capacidad,5), probs_asociada





def calcProbabilidadError(probsPriori: list[float], matriz: list[list[float]]) -> float:
    """

    Un problema que surge con los canales es transmitir mensajes confiables por
    canales no confiables, ante esto se estableces "reglas de decision" para decidir que 
    simbolo de salida se corresponderia con tal simbolo de entrada.
    Cada canal tiene r elevado a s reglas diferentes (r entradas posibles y s salidas posibles).

    ¿Cual se debe escoger?
    Se elegira la que haga la minima probabilidad de error

    Ej:

    El canal tiene tres entradas a1, a2, a3 y tres salidas b1, b2, b3. ¿Qué
    símbolo de entrada corresponde a un símbolo de salida recibido?
    Dos reglas de decisión del canal podrían ser:
    1.              2.
    d(b1)=a1        d(b1)=a1
    d(b2)=a2        d(b1)=a2
    d(b3)=a3        d(b1)=a2


    La probabilidad de error es el valor medio de P(E/Bi), es decir, el promedio
    de los valores de que dada una salida me haya equivocado

    Pe = Σ P(E/Bi) * P(Bi)

    La probabilidad de error sera minima con la regla de desicion que asigne 
    a cada simbolo de salida el simbolo de entrada de mayor probabilidad 
    (Esta regla es la regla de maxima posibilidad condicional)



    Para encontrar esa probabilidad de error se hace un pasaje de terminos y calculos
    con bayes y se llega a

    Pe = (1 / r) * ∑ P(b /a)

    r es la cantidad de simbolos de entrada y la sumatoria es sobre toda la matriz menos
    las P(bj / ai) en los que las P(bj / ai) son maximas por columna (Es decir, las que se eligieron
    en la regla de decision de maxima posibilidad condicional)
    El conjunto de todas las probabilidades condicionales maximas es a*



    Explicacion del codigo:
    1. Recorro cada columna de la matriz
    2. Para cada columna, encuentro el indice del valor maximo
    3. Almaceno los indices de los valores maximos en una lista
    4. Inicializo la variable probabilidadError en 0
    5. Recorro cada columna de la matriz
    6. Para cada columna, recorro cada fila de la matriz
    7. Si el indice de la fila no es igual al indice del valor maximo,
       sumo a la variable probabilidadError el producto de la probabilidad
       a priori de la fila por el valor de la matriz en esa posicion
    8. Devuelvo la variable probabilidadError



    Conclusion:
    Si la Pe es 1, y el canal es BSC, se pueden "invertir" los resultados
    para saber cuales eran las salidas correctas. Sino es BSC el canal
    da todos los resultados mal, no se pueden invertir si hay mas de 2
    salidas

    Si la Pe es 0 entonces el canal es sin ruido y no hay errores


    Version Laureano
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




# Version Proia
def error_canal(matriz, probs_priori):
    error = 0
    lista_d = []
    for j in range(len(matriz[0])):
        max = 0
        indice = -1
        for i in range(len(matriz)):
            if (matriz[i][j]>max):
                max = matriz[i][j]
                indice = i
        lista_d.append(indice)
    for i in range(len(matriz)):
        suma = 0
        for j in range(len(matriz[0])):
            if (lista_d[j]!=i):
                suma += probs_priori[i]*matriz[i][j]
        error += suma
    return round(error,5)