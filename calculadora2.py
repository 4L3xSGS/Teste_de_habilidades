"""Entrada histórica: execute com uv run python calculadora2.py."""

from habilidades.calculator import calculate


def somar(a: float, b: float) -> float:
    return calculate(a, b, "+")


def subtrair(a: float, b: float) -> float:
    return calculate(a, b, "-")


def multiplicar(a: float, b: float) -> float:
    return calculate(a, b, "*")


def dividir(a: float, b: float) -> float:
    return calculate(a, b, "/")


def main() -> None:
    try:
        operation = input("Escolha a operação (+ - * /): ").strip()
        a = float(input("Primeiro número: ").replace(",", "."))
        b = float(input("Segundo número: ").replace(",", "."))
        print(f"Resultado: {calculate(a, b, operation):g}")
    except (ValueError, EOFError, KeyboardInterrupt) as error:
        print(f"Operação encerrada: {error}")


if __name__ == "__main__":
    main()
