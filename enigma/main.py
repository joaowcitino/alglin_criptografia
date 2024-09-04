import numpy as np
from flask import Flask, request, jsonify

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

app = Flask(__name__)

def gerar_matriz_permutacao(alfabeto_len):
    P = np.eye(alfabeto_len)
    np.random.shuffle(P)
    return P

@app.route('/criptografia', methods=['POST'])
def criptografia():
    data = request.get_json()
    mensagem = data.get('mensagem')
    
    if not mensagem:
        return jsonify({'error': 'Mensagem não fornecida'}), 400

    alfabeto = "abcdefghijklmnopqrstuvwxyz "
    alfabeto_len = len(alfabeto)
    
    if any(char not in alfabeto for char in mensagem.lower()):
        return jsonify({'error': 'A mensagem contém caracteres inválidos'}), 400

    P = gerar_matriz_permutacao(alfabeto_len)
    E = gerar_matriz_permutacao(alfabeto_len)
    
    mensagem_cifrada = cifrar(mensagem, P, alfabeto)
    print(f"Mensagem cifrada: {mensagem_cifrada}")
    
    mensagem_decifrada = de_cifrar(mensagem_cifrada, P, alfabeto)
    print(f"Mensagem decifrada: {mensagem_decifrada}")

    mensagem_cifrada_enigma = enigma(mensagem, P, E, alfabeto)
    print(f"Mensagem cifrada com Enigma: {mensagem_cifrada_enigma}")
    
    mensagem_decifrada_enigma = de_enigma(mensagem_cifrada_enigma, P, E, alfabeto)
    print(f"Mensagem decifrada com Enigma: {mensagem_decifrada_enigma}")
    
    return jsonify({'mensagem_cifrada': mensagem_cifrada_enigma, 'mensagem_decifrada': mensagem_decifrada, 'mensagem_cifrada_enigma': mensagem_cifrada_enigma, 'mensagem_decifrada_enigma': mensagem_decifrada_enigma })

if __name__ == '__main__':
    app.run(debug=True)