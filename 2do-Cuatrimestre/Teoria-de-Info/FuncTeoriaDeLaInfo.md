**Descripción**
- **Módulo**: `FuncTeoriaDeLaInfo.py` — Colección de utilidades para teoría de la información: cálculo de entropías, generación de alfabetos y mensajes, cadenas de Markov, códigos (Huffman, Shannon-Fano), codificación/decodificación, paridad y análisis de canales.

**Uso rápido**
- **Archivo**: `FuncTeoriaDeLaInfo.py` — importar funciones con `from FuncTeoriaDeLaInfo import <funcion>`.

**Funciones y explicación**

**Generales / Utilidades**
- **Función**: `mostrarMatriz(matriz, titulo)` : Imprime `titulo` y muestra fila por fila la `matriz` (útil para debug).
- **Función**: `max_vector(vector)` : Devuelve el máximo de `vector` (wrapper para `max`).
- **Función**: `diferencia(v1, v2)` : Devuelve lista con diferencias absolutas elemento a elemento entre `v1` y `v2`.

**Probabilidades y entropía**
- **Función**: `getInformacion(probabilidades)` : Para cada probabilidad p > 0 retorna `log2(1/p)`, y 0 para p==0. Devuelve lista de informaciones por símbolo.
- **Función**: `getEntropia(probabilidades)` : Calcula H = sum p * I(p) usando `getInformacion` (entropía en bits).
- **Función**: `getEntropiaBinariaW(w)` : Entropía para alfabeto binario con probabilidad `w` (usa `getEntropia([w,1-w])`).

**Alfabeto y mensajes**
- **Función**: `getAlfabetoyProbabilidades(cadena)` : Dado un `cadena` retorna `(alfabeto, probabilidades)` ordenados por símbolo. Cuenta apariciones y normaliza.
- **Función**: `generarMensajeAlfabeto(alfabeto, probabilidades, n)` : Genera una cadena de longitud `n` muestreando según `probabilidades` del `alfabeto`.
- **Función**: `generarMensajeCodigo(palabras_codigo, probabilidades, n)` : Genera mensaje codificado concatenando `n` palabras de `palabras_codigo` seleccionadas por `probabilidades`.
- **Función**: `probabilidadesOrdenN(probs, N)` : Calcula las probabilidades de la extensión de orden `N` (producto cartesiano de probabilidades).

**Extensiones y combinaciones**
- **Función**: `calcExtensionN(fuente, probabilidades, n)` : Construye la extensión de grado `n` de la fuente (listas de combinaciones y sus probabilidades).

**Cadenas y Markov**
- **Función**: `getMatrizconCad(cadena)` : A partir de `cadena` calcula alfabeto ordenado y matriz de transición (conteos normalizados por columna).
- **Función**: `calcTransitions(msg, alphabet, i, j)` : Cuenta transiciones `alphabet[i] -> alphabet[j]` en `msg` (contador simple).
- **Función**: `getMatriz(alphabet, msg)` : Otra versión para construir la matriz de transición desde `msg` y `alphabet` (normaliza y redondea a 2 decimales).
- **Función**: `getCadenaConMatriz(matriz, alfabeto, n)` : Genera una cadena de longitud `n` siguiendo la matriz de Markov `matriz` y `alfabeto`.
- **Función**: `getVecEstacionarioMat(matriz)` : Calcula iterativamente un vector estacionario aproximado (potencia) de la matriz (vector columna con suma 1 inicializada uniformemente).
- **Función**: `calcularEntropiaFuenteMarkov(mat, vec_est)` : Entropía de la fuente con memoria H = sum_j v_j * (sum_i p(i|j)*log2(1/p(i|j))).
- **Función**: `isMemoriaNula(matriz, tolerancia)` : Devuelve True si la máxima diferencia entre entradas de cada columna < `tolerancia` (fuente sin memoria).

**Códigos y propiedades (no singular, instantáneo, unívoco, Kraft, etc.)**
- **Función**: `isNoSingular(codigo)` : True si todas las palabras en `codigo` son distintas.
- **Función**: `isInstantaneo(codigo)` : True si ninguna palabra es prefijo de otra (código prefijo).
- **Función**: `isUnivoco(codigo)` : Implementa el algoritmo de Sardinas–Patterson para decidir si `codigo` es unívocamente decodificable.
- **Función**: `getTipoCodigo(codigo)` : Clasifica el tipo de código consultando las funciones anteriores (retorna texto descriptivo).
- **Función**: `getAlfabetoCodigo(codigo)` : Devuelve el conjunto de símbolos usados en el `codigo`.
- **Función**: `getLongitudesPalabrasCod(codigo)` : Lista de longitudes de cada palabra del `codigo`.
- **Función**: `getKraft(alfabeto, longitud)` : Calcula la suma de Kraft sum r^{-l_i} (r = tamaño de `alfabeto`).
- **Función**: `getEntropiaCodigoR(codigo, probabilidad)` : Entropía del código con log base `r` (r = tamaño del alfabeto de código).
- **Función**: `getLongitudMedia(palabras_codigo, probabilidad)` : Longitud media L = sum p_i * l_i.
- **Función**: `isCompacto(palabras_codigo, probabilidad)` : True si el código es instantáneo y cada longitud cumple l_i <= ceil(log_r(1/p_i)).

**Generación y algoritmos de codificación**
- **Función**: `getCodigoHuffman(probs)` : Implementación iterativa de Huffman que retorna lista de códigos binarios por índice de `probs`.
- **Función**: `getCodigoShannonFano(probs)` : Implementación recursiva de Shannon–Fano (división por balance de probabilidades).
- **Función**: `generarCodigoShannonFano(probabilidades)` : Variante alternativa (otra implementación) para Shannon–Fano.
- **Función**: `shannonfano` / `propagateSubfix` / `getSortedIndex` : utilidades internas alternativas usadas por implementaciones de Shannon–Fano.
- **Función**: `verificar_primer_teorema(probabilidades, codigo, N)` : Verifica el primer teorema de Shannon para orden `N` comparando H y L/N.

**Rendimiento y redundancia**
- **Función**: `calcularRendimiento(probabilidades, codigo)` : R = H / L (si L != 0).
- **Función**: `calcularRedundancia(probabilidades, codigo)` : D = 1 - R (redundancia del código).

**Codificación en bits / empaquetado**
- **Función**: `codeMessage(codigo, mensaje, alfabeto=[])` : Codifica `mensaje` usando `codigo` y `alfabeto`, devuelve `bytearray` con primer byte = cantidad de bits de relleno añadidos al final.
- **Función**: `decodeMessage(alfabeto, codigo, byte_array)` : Decodifica `byte_array` (codificado por `codeMessage`) devolviendo el `mensaje` original.
- **Función**: `calcularTasaCompresion(mensaje, mensajeCodificado)` : Retorna razón tamaño_original / tamaño_codificado (en bits).
- **Función**: `createFile(name, byte_array)` : Guarda `byte_array` en disco como `name`.
- **Función**: `readFile(name)` : Lee y retorna `bytearray` desde `name`.

**Compresión simple y RLC**
- **Función**: `compressRLCToBytes(mensaje)` : Implementa Run-Length Encoding simple, retorna `bytearray` con pares (ASCII del símbolo, contador).

**Distancia Hamming y corrección básica**
- **Función**: `distanciaHamming(codigo)` : Calcula distancia de Hamming mínima entre todas las parejas de palabras del `codigo` (asume mismas longitudes).
- **Función**: `erroresDetectables(codigo)` : Número máximo de errores detectables = d - 1.
- **Función**: `erroresCorregibles(codigo)` : Número máximo de errores corregibles = floor((d - 1) / 2).

**Paridad y control de errores (VRC / LRC)**
- **Función**: `agregarBitParidadPalabra(palabra)` : Dada una cadena binaria añade bit de paridad (paridad par) al final.
- **Función**: `charToAsciiWithParity(char)` : Convierte `char` a 7 bits ASCII + bit de paridad VRC y lo retorna como entero.
- **Función**: `stringToByteArrayWithParity(s)` : Convierte cadena `s` a `bytearray` con paridad VRC por carácter y añade byte de paridad longitudinal (LRC) al inicio.
- **Función**: `byteArrayToStringWithParity(byte_array)` : Intenta verificar y corregir (si posible) errores usando VRC+LRC, devuelve la cadena original o cadena vacía si no puede corregir.
- **Función**: `convertMatrixToByteArray(matriz)` : Convierte una matriz de bits a `bytearray` interpretando cada fila como byte.

**Canales (matrices), probabilidades y entropías condicionales**
- **Función**: `getMatrizCanal(entrada, salida)` : Construye matriz P(bj|ai) contando pares en `entrada`/`salida` (ambas cadenas mismas longitudes).
- **Función**: `getProbabilidadesSalida(probsPriori, matrizCanal)` : Calcula P(bj) = sum_i P(ai) * P(bj|ai).
- **Función**: `getProbabilidadesSalidaConMsg(entrada, salida)` : Igual que anterior pero calcula internamente la matriz y las probabilidades a priori desde `entrada`.
- **Función**: `getMatrizSucesosSimultaneos(probsPriori, matrizCanal)` : Calcula P(ai,bj) = P(ai) * P(bj|ai) (matriz).
- **Función**: `getProbabilidadesAPosteriori(probsPriori, matrizCanal, probs_salida)` : Calcula P(ai|bj) usando Bayes.
- **Función**: `getEntropiasAPosteriori(probsPriori, matrizCanal)` : Calcula H(A|bj) para cada salida bj.
- **Función**: `getEquivocacionRuido(probsPriori, matrizCanal)` : Calcula H(A|B) = sum_{a,b} P(a,b) log2(1/P(a|b)).
- **Función**: `getPerdida(probsPriori, matrizCanal)` : Calcula H(B|A) = sum_a P(a) H(B|a).
- **Función**: `getEntropiaAfín(probsPriori, matrizCanal)` : Calcula H(A,B) por definición sobre P(a,b).
- **Función**: `getInformacionMutua(probsPriori, matrizCanal)` : Calcula I(A;B) = sum_{a,b} P(a,b) log2(P(a,b)/(P(a)P(b))).
- **Función**: `verificarRelaciones(probsPriori, matrizCanal)` : Comprueba algunas relaciones entre H(A), H(B), H(A|B), H(B|A), H(A,B) e I(A;B).

**Propiedades de canales y reducción**
- **Función**: `isSinRuido(matriz)` : True si cada columna tiene exactamente un elemento no nulo (exactamente un 1 en cada columna).
- **Función**: `isDeterminante(matriz)` : True si cada fila tiene exactamente un 1 y el resto ceros (canal determinante).
- **Función**: `getCanalCompuesto(canalA, canalB)` : Multiplica matrices para obtener el canal en serie (A seguido de B).
- **Función**: `verificarColumnasReducibles(matriz, col1, col2)` : Determina si dos columnas son reducibles (proporcionales fila a fila con manejos de ceros).
- **Función**: `generarMatrizDeterminante(matriz, col1, col2)` : Construye matriz determinante que combina `col1` y `col2` en una columna.
- **Función**: `maxReduccion(matriz)` : Ejecuta reducciones sucesivas sobre la matriz del canal aplicando `verificarColumnasReducibles` + `generarMatrizDeterminante` hasta no poder reducir más.
- **Función**: `isSimetrico(matriz)` : Determina si el canal es simétrico (filas y columnas son permutaciones de la primera fila/columna).
- **Función**: `isUniforme(matriz)` : True si cada fila es permutación de la primera fila.
- **Función**: `isCanalBSC(matriz)` : Detecta canal BSC (2x2 con probabilidad de error simétrica).

**Capacidad y probabilidades de error**
- **Función**: `calcCapacidad(matriz)` : Calcula la capacidad para casos especiales (determinante, sin ruido, simétrico, uniforme, BSC). Para casos generales no maximiza sobre distribuciones.
- **Función**: `estimarCapacidadCanalBinario(matriz, paso)` : Para canales binarios recorre p en [0,1] con `paso` y estima la capacidad máxima por búsqueda discreta de I(A;B).
- **Función**: `calcProbabilidadError(probsPriori, matriz)` : Tomando regla de máxima verosimilitud por columna calcula P(e) sumando probabilidades asociadas a decisiones erróneas.

**Notas finales**
- Algunos métodos tienen variantes (por ejemplo varias implementaciones de Shannon–Fano). Revisar el código fuente para ejemplos adicionales.
- Esta documentación es un resumen. Para ejemplos concretos o pruebas, dime qué funciones quieres que documente con ejemplos o que escriba tests/ejemplos.

**Archivo generado**: `FuncTeoriaDeLaInfo.md`
