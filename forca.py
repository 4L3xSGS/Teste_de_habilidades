"""Entrada histórica da forca; regras e interface ficam no pacote habilidades."""

from habilidades.cli import main
from habilidades.cli import play_hangman as jogar_forca
from habilidades.games import choose_word as escolher_palavra

__all__ = ["escolher_palavra", "jogar_forca"]

if __name__ == "__main__":
    raise SystemExit(main(["forca"]))
