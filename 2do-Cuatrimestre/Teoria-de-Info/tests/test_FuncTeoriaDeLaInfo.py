import sys
import os
import math
import random

# Aseguro que el path del repo esté en sys.path para poder importar el módulo
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from FuncTeoriaDeLaInfo import (
    getInformacion,
    getEntropia,
    getAlfabetoyProbabilidades,
    getCodigoHuffman,
    getCodigoShannonFano,
    codeMessage,
    decodeMessage,
    distanciaHamming,
    getVecEstacionarioMat,
    getMatrizCanal,
    getProbabilidadesSalida,
    getInformacionMutua,
    stringToByteArrayWithParity,
    byteArrayToStringWithParity,
)


def test_getInformacion_and_entropia():
    probs = [0.5, 0.5]
    info = getInformacion(probs)
    assert info == [1.0, 1.0]
    H = getEntropia(probs)
    assert math.isclose(H, 1.0, rel_tol=1e-9)


def test_getAlfabetoyProbabilidades():
    s = 'aab'
    alf, probs = getAlfabetoyProbabilidades(s)
    # alfabeto ordenado 'a','b'
    assert tuple(alf) == ('a', 'b')
    assert tuple(round(p, 6) for p in probs) == (round(2/3, 6), round(1/3, 6))


def test_huffman_code_lengths():
    probs = [0.5, 0.25, 0.15, 0.10]
    codes = getCodigoHuffman(probs)
    lengths = sorted(len(c) for c in codes)
    assert lengths == [1, 2, 3, 3]


def test_shannonfano_code_lengths():
    probs = [0.4, 0.3, 0.2, 0.1]
    codes = getCodigoShannonFano(probs)
    lengths = sorted(len(c) for c in codes)
    assert lengths == [1, 2, 3, 3]


def test_code_and_decode_message():
    alfabeto = ['A', 'B']
    codigo = ['0', '1']
    mensaje = 'ABBA'
    # reproducible behavior no necesaria aquí porque no hay aleatoriedad
    b = codeMessage(codigo, mensaje, alfabeto)
    decoded = decodeMessage(alfabeto, codigo, b)
    assert decoded == mensaje


def test_distancia_hamming():
    codes = ['000', '111', '101']
    # minimal hamming distance among pairs is 1 (between '111' and '101')
    assert distanciaHamming(codes) == 1


def test_vec_estacionario_identidad():
    # Matriz identidad 2x2 => vector estacionario uniforme
    M = [[1, 0], [0, 1]]
    v = getVecEstacionarioMat(M)
    assert len(v) == 2
    assert math.isclose(v[0], 0.5, rel_tol=1e-6)
    assert math.isclose(v[1], 0.5, rel_tol=1e-6)


def test_channel_and_mutual_information():
    # Canal determinista A->0, B->1
    entrada = 'ABAB'
    salida = '0101'
    canal = getMatrizCanal(entrada, salida)
    # probabilidades a priori uniformes
    probsPriori = getAlfabetoyProbabilidades(entrada)[1]
    probsSalida = getProbabilidadesSalida(probsPriori, canal)
    # salida igualmente probable
    assert all(math.isclose(p, 0.5, rel_tol=1e-9) for p in probsSalida)
    # Información mutua para canal determinista debe ser la entropía H(A) = 1 bit
    I = getInformacionMutua(probsPriori, canal)
    assert math.isclose(I, 1.0, rel_tol=1e-9)


def test_parity_roundtrip():
    s = 'Hi'
    ba = stringToByteArrayWithParity(s)
    out = byteArrayToStringWithParity(ba)
    assert out == s
