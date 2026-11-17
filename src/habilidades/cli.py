"""Interface em português: argparse, JSON para automação e códigos de saída."""

import argparse
import json
import sys
from collections.abc import Sequence

from habilidades import __version__
from habilidades.calculator import calculate
from habilidades.games import choose_word, flip_coin, roll_dice
from habilidades.hangman import Hangman
from habilidades.passwords import generate_password


def parser() -> argparse.ArgumentParser:
    """Constrói comandos sem executar lógica de domínio."""
    root = argparse.ArgumentParser(
        prog="habilidades", description="Python Lab · fundamentos aplicados, por Alexander Souto"
    )
    root.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    commands = root.add_subparsers(dest="command", required=True)
    calculator = commands.add_parser("calcular", help="Operações aritméticas")
    calculator.add_argument("a", type=float)
    calculator.add_argument("operation", choices=["+", "-", "*", "/"])
    calculator.add_argument("b", type=float)
    coin = commands.add_parser("moeda", help="Cara ou coroa")
    coin.add_argument("--escolha", choices=["cara", "coroa"])
    dice = commands.add_parser("dados", help="Lançar dados configuráveis")
    dice.add_argument("--quantidade", type=int, default=2)
    dice.add_argument("--faces", type=int, default=6)
    password = commands.add_parser("senha", help="Gerar senha local com secrets")
    password.add_argument("--tamanho", type=int, default=16)
    password.add_argument("--sem-maiusculas", action="store_true")
    password.add_argument("--sem-numeros", action="store_true")
    password.add_argument("--sem-simbolos", action="store_true")
    commands.add_parser("forca", help="Iniciar partida interativa")
    for command in (calculator, coin, dice, password):
        command.add_argument("--json", action="store_true", help="Saída estruturada para automação")
    return root


def play_hangman() -> None:
    """Executa a interação, mantendo o estado independente da apresentação."""
    game = Hangman(choose_word())
    print("FORCA · descubra a palavra com até 6 erros. Ctrl+C para sair.")
    while not game.finished:
        print(f"\n{game.masked}  |  Tentativas restantes: {game.remaining}")
        print(f"Letras usadas: {', '.join(sorted(game.guesses)) or 'nenhuma'}")
        try:
            letter = input("Digite uma letra: ")
            if letter.strip().lower() in game.guesses:
                print("Você já tentou essa letra.")
            game = game.guess(letter)
        except ValueError as error:
            print(error)
    print(f"{'Você venceu!' if game.won else 'Fim de jogo.'} Palavra: {game.word}")


def main(argv: Sequence[str] | None = None) -> int:
    """Retorna 0 em sucesso, 2 em entrada inválida e 130 em interrupção."""
    args = parser().parse_args(argv)
    try:
        payload: dict[str, object]
        match args.command:
            case "calcular":
                result = calculate(args.a, args.b, args.operation)
                payload = {"resultado": result}
                text = f"Resultado: {result:g}"
            case "moeda":
                face = flip_coin()
                payload = {"resultado": face}
                text = f"Resultado: {face}"
                if args.escolha:
                    correct = args.escolha == face
                    payload["acertou"] = correct
                    text += " · Você acertou!" if correct else " · Tente novamente!"
            case "dados":
                rolls = roll_dice(args.quantidade, args.faces)
                payload = {"dados": rolls, "soma": sum(rolls)}
                text = f"Dados: {', '.join(map(str, rolls))} · Soma: {sum(rolls)}"
            case "senha":
                password = generate_password(
                    args.tamanho,
                    uppercase=not args.sem_maiusculas,
                    digits=not args.sem_numeros,
                    symbols=not args.sem_simbolos,
                )
                payload = {"senha": password}
                text = password
            case _:
                play_hangman()
                return 0
        print(json.dumps(payload, ensure_ascii=False) if args.json else text)
        return 0
    except ValueError as error:
        print(f"Erro: {error}", file=sys.stderr)
        return 2
    except (KeyboardInterrupt, EOFError):
        print("\nExecução interrompida.", file=sys.stderr)
        return 130
