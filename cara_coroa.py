import random
def jogar():
    print("Bem-vindo ao jogo de Cara ou Coroa!")
    escolha_usuario = input("Escolha 'cara' ou 'coroa': ").strip().lower()

    if escolha_usuario not in ['cara', 'coroa']:
        print("Escolha inválida. Tente novamnete.")
        return
    resultado = random.choice(['cara', 'coroa'])
    print(f"O resultado foi: {resultado}")

    if escolha_usuario == resultado:
        print("Você acertou!!")
    else:
        print("Você errou...")

#executar o jogo
jogar()
