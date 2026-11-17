"""Entrada histórica: dois dados de seis faces."""

from habilidades.cli import main as cli_main


def jogar_dados() -> None:
    cli_main(["dados"])


def main() -> None:
    try:
        while True:
            input("Pressione Enter para lançar os dados…")
            jogar_dados()
            if input("Jogar novamente? (s/n): ").strip().lower() != "s":
                break
    except (EOFError, KeyboardInterrupt):
        print("\nPartida encerrada.")


if __name__ == "__main__":
    main()
