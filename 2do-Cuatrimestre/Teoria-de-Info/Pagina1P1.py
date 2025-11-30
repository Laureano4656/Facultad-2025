import FuncTeoriaDeLaInfo as util

msg1 = "+-/+/-//-/*-/**-*---////-+--*+*/-----/--+/++--*/-+"
alfabeto1,dist_prob1 = util.getAlfabetoyProbabilidades(msg1)

print("Distribucion de probabilidades mensaje 1: ",dist_prob1)

matMsg1 = util.getMatriz(alfabeto1,msg1)

print("Alfabeto mensaje 1: ",alfabeto1)

print("Es memoria nula: ",util.isMemoriaNula(matMsg1,0.01))

print("Matriz mensaje 1")
for fila in matMsg1:
    print(fila)

print("Entropia msg1: ",util.getEntropia(dist_prob1))

nuevaFuente1,nuevasProbs1 = util.calcExtensionN(alfabeto1,dist_prob1,2)

print("Alfabeto extension 2: ",nuevaFuente1)
print("Probabilidades extension 2: ",nuevasProbs1)
print("Entropia extension 2: ",util.getEntropia(nuevasProbs1))
print("--------------------------------------------")

msg2 = "-+-+*//++///*/-////+---////-+/+--+-+/-/+-+/-+*++//"

alfabeto2,dist_prob2 = util.getAlfabetoyProbabilidades(msg2)
print("Alfabeto mensaje 2: ",alfabeto2)
print("Distribucion de probabilidades mensaje 2: ",dist_prob2)

matMsg2 = util.getMatriz(alfabeto2,msg2)

print("Matriz de mensaje 2:")

for fila in matMsg2:
    print(fila)

print("Es memoria nula: ",util.isMemoriaNula(matMsg2,0.01))
# debo calcular la entropia con la matriz
print("Vector estacionario mensaje 2: ",util.getVecEstacionarioMat(matMsg2))

print("Entropia msg2: ",util.calcularEntropiaFuenteMarkov(matMsg2,util.getVecEstacionarioMat(matMsg2)))
