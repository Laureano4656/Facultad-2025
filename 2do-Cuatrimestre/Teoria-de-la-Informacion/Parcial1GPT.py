import utilP1 as ut

## Ejercicio 2

dist_prob = [0.5,0.25,0.125,0.125]
print("Entropia de la distribucion de probabilidad dada: ", ut.entropia(dist_prob))

## Ejercicio 3

dist_prob = [0.9,0.1]
fuenteExtendida,dist_prob = ut.calcular_extension_n(["A","B"],dist_prob, 3)
print("Entropia de la fuente original: ", ut.entropia([0.9,0.1]))
print("Entropia de la fuente extendida: ", ut.entropia(dist_prob))

## Ejercicio 4
dist_prob = [[0.9,0.1],[0.4,0.6]]
print("Entropia de la fuente de Markov: ", ut.entropia_con_vector(dist_prob,ut.vector_estacionario(dist_prob,2),2))
print("Entropia de fuente binaria equiprobable: ", ut.entropia([0.5,0.5]))