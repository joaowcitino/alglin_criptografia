import numpy as np
from enigma import cifrar, de_cifrar, enigma, de_enigma

def gerar_matriz_permutacao(alfabeto_len):
    P = np.eye(alfabeto_len)
    np.random.shuffle(P)
    return P

def demo():
    alfabeto = "abcdefghijklmnopqrstuvwxyz "
    alfabeto_len = len(alfabeto)

    mensagem = input("Digite a mensagem que deseja cifrar: ").lower()

    if any(char not in alfabeto for char in mensagem):
        print("A mensagem contém caracteres que não fazem parte do alfabeto permitido.")
        return

    P = gerar_matriz_permutacao(alfabeto_len)
    E = gerar_matriz_permutacao(alfabeto_len)

    mensagem_cifrada = cifrar(mensagem, P, alfabeto)
    print(f"Mensagem cifrada: {mensagem_cifrada}")
    
    mensagem_decifrada = de_cifrar(mensagem_cifrada, P, alfabeto)
    print(f"Mensagem decifrada: {mensagem_decifrada}")

    # Cifra e decifra com Enigma
    mensagem_cifrada_enigma = enigma(mensagem, P, E, alfabeto)
    print(f"Mensagem cifrada com Enigma: {mensagem_cifrada_enigma}")
    
    mensagem_decifrada_enigma = de_enigma(mensagem_cifrada_enigma, P, E, alfabeto)
    print(f"Mensagem decifrada com Enigma: {mensagem_decifrada_enigma}")

if __name__ == "__main__":
    demo()
