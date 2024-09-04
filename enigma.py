import numpy as np

def para_one_hot(msg: str, alfabeto: str):
    N = len(alfabeto)
    T = len(msg)
    M = np.zeros((N, T))
    for i, char in enumerate(msg):
        idx = alfabeto.index(char)
        M[idx, i] = 1
    return M

def para_string(M: np.array, alfabeto: str):
    msg = ''
    for col in range(M.shape[1]):
        idx = np.argmax(M[:, col])
        msg += alfabeto[idx]
    return msg

def cifrar(msg: str, P: np.array, alfabeto: str):
    M = para_one_hot(msg, alfabeto)
    M_cifrada = P @ M
    return para_string(M_cifrada, alfabeto)

def de_cifrar(msg: str, P: np.array, alfabeto: str):
    M_cifrada = para_one_hot(msg, alfabeto)
    M_decifrada = np.linalg.inv(P) @ M_cifrada
    return para_string(M_decifrada, alfabeto)

def enigma(msg: str, P: np.ndarray, E: np.ndarray, alfabeto: str) -> str:
    matriz_mensagem = para_one_hot(msg, alfabeto)
    encriptador = P.copy() 
    matriz_encriptada = np.zeros_like(matriz_mensagem)

    for i in range(matriz_mensagem.shape[1]):
        matriz_encriptada[:, i] = encriptador @ matriz_mensagem[:, i]
        encriptador = E @ encriptador

    return para_string(matriz_encriptada, alfabeto)

def de_enigma(msg: str, P: np.ndarray, E: np.ndarray, alfabeto: str) -> str:
    matriz_mensagem_encriptada = para_one_hot(msg, alfabeto)
    decriptador = np.linalg.inv(P).copy()
    matriz_decriptada = np.zeros_like(matriz_mensagem_encriptada)

    for i in range(matriz_mensagem_encriptada.shape[1]):
        matriz_decriptada[:, i] = decriptador @ matriz_mensagem_encriptada[:, i]
        decriptador = decriptador @ np.linalg.inv(E)

    return para_string(matriz_decriptada, alfabeto)







