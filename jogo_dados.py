import random

def jogar_dados():
    dado1 = random.randint(1,6)
    dado2 = random.randint(1,6)

    print(f"Você lançou os dados!")
    print(f"Dado 1: {dado1}")
    print(f"Dado 2: {dado2}")
    print(f"Soma dos dados: {dado1 + dado2}")

def main():
    while True:
        input("Pressione Enter para lançar os dados...")
        jogar_dados()
        continuar = input("Deseja jogar novamente? (s/n): ").lower()
        if continuar != 's':
            print("Obrigado por Jogar!")
            break
if __name__ == "__main__":
    main()
