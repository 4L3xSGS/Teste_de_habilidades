import random

def escolher_palavra():
    palavras = ['python', 'programa' 'desenvolvedor', 'computador', 'algoritmo']
    return random.choice(palavras).lower()

def jogar_forca():
    palavra = escolher_palavra()
    letras_descobertas = ['_' for _ in palavra]
    letras_usadas = set()
    tentativas = 6

    print("Bem-vindo ao Jogo da Forca!")
    print("A palavra tem", len(palavra), "letras.")

    while tentativas >0 and '_' in letras_descobertas:
        print("\nPalavra:", ' '.join(sorted(letras_usadas)))
        print("Letras usadas:", ', '.join(sorted(letras_usadas)))
        print("Tentativas restantes:", tentativas)

        letra=input("Digite uma letra: ").lower()

        if not letra.isalpha() or len(letra) !=1:
            print("Digite apenas uma letra válida.")
            
        if   letra in letras_usadas:
            print("Você já tentou essa letra.")
            continue

        letras_usadas.add(letra)

        if letra in palavra:
            for i, l in enumerate(palavra):
                if l == letra:
                    letras_descobertas[i] = letra
            print("Boa!! A Letra está na palavra.")
        else:
            tentativa -= 1
            print("Ops!! A letra não está na palavra.")

    if '_' not in letras_descobertas:
        print("\n Parabéns!! Você descobriu a palavra:", palavra)
    else:
        print("\n Fim de jogo!! A Palavra era", palavra)

if __name__ == "__main--":
    jogar_forca()