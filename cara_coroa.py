"""Entrada histórica, sem efeitos colaterais ao importar."""

from habilidades.cli import main


def jogar() -> None:
    try:
        choice = input("Escolha 'cara' ou 'coroa': ").strip().lower()
        if choice not in {"cara", "coroa"}:
            print("Escolha inválida. Use cara ou coroa.")
            return
        main(["moeda", "--escolha", choice])
    except (EOFError, KeyboardInterrupt):
        print("\nPartida encerrada.")


if __name__ == "__main__":
    jogar()
