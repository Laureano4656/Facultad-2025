import FuncTeoriaDeLaInfo as util
dist_prob1 = [0.15,0.25,0.05,0.45,0.1]
cod1 = ["/+","*","+-","-","*/"]
alfabetoCod1 = util.getAlfabetoCodigo(cod1)

print("Alfabeto codigo 1: ",alfabetoCod1)

print("Entropia codigo 1: ",util.getEntropiaCodigoR(cod1,dist_prob1))

print("Longitud media codigo 1: ",util.getLongitudMedia(cod1,dist_prob1))
print("Longitudes palabras codigo 1: ",util.getLongitudesPalabrasCod(cod1))
print("Inecuacion Kraft-Mc Millan: ",util.getKraft(alfabetoCod1,util.getLongitudesPalabrasCod(cod1)))

print("El codigo es no singular: ",util.isNoSingular(cod1))
print("El codigo es unequivoco: ",util.isUnivoco(cod1))
print("El codigo es instantaneo: ",util.isInstantaneo(cod1))
print("El codigo es compacto: ",util.isCompacto(cod1,dist_prob1))

print("-------------------------------------------------")

dist_prob2 = [0.15,0.25,0.05,0.45,0.1]
cod2 = [",;" , ";" , ":." , "." , ",:"]

alfabetoCod2 = util.getAlfabetoCodigo(cod2)

print("Alfabeto codigo 2: ",alfabetoCod2)

print("Entropia codigo 2: ",util.getEntropiaCodigoR(cod2,dist_prob2))
print("Longitud media codigo 2: ",util.getLongitudMedia(cod2,dist_prob2))

print("Inecuacion Kraft-Mc Millan: ",util.getKraft(alfabetoCod2,util.getLongitudesPalabrasCod(cod2)))

print("El codigo es no singular: ",util.isNoSingular(cod2))
print("El codigo es unequivoco: ",util.isUnivoco(cod2))
print("El codigo es instantaneo: ",util.isInstantaneo(cod2))
print("El codigo es compacto: ",util.isCompacto(cod2,dist_prob2))