
def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: divisão por zero"
    return a / b

def main():
    print("Calculadora Simples")
    print("Operações disponíveis: +, -, *, /")

    operacao = input("Escolha a operação (+ - * /): ")
    a = float(input("Digite o primeiro número: "))
    b = float(input("Digite o segundo número: "))

    if operacao == '+':
        resultado = somar(a,b)
    elif operacao == '-':
        resultado = subtrair(a,b)
    elif operacao == '*':
        resultado = multiplicar(a,b)
    elif operacao == '/':
        resultado = dividir(a,b)
    else:
        resultado = "Operação inválida"

    print(f"Resultado: {resultado}")

if __name__ == "__main__":
    main()