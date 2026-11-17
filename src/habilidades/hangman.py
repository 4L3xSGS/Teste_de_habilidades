"""Estado imutável da forca: nenhuma leitura de terminal na regra do jogo."""

import string
from dataclasses import dataclass


@dataclass(frozen=True)
class Hangman:
    """Cada palpite válido devolve um novo estado; repetidos não consomem tentativas."""

    word: str
    guesses: frozenset[str] = frozenset()
    max_mistakes: int = 6

    def __post_init__(self) -> None:
        if not self.word or any(letter not in string.ascii_lowercase for letter in self.word):
            raise ValueError("A palavra deve conter apenas letras minúsculas de a a z.")
        if isinstance(self.max_mistakes, bool) or self.max_mistakes < 1:
            raise ValueError("O número de tentativas precisa ser positivo.")
        if any(len(letter) != 1 or letter not in string.ascii_lowercase for letter in self.guesses):
            raise ValueError("Os palpites devem ser letras de a a z.")

    @property
    def remaining(self) -> int:
        return max(0, self.max_mistakes - len(self.guesses.difference(self.word)))

    @property
    def won(self) -> bool:
        return set(self.word).issubset(self.guesses)

    @property
    def finished(self) -> bool:
        return self.won or self.remaining == 0

    @property
    def masked(self) -> str:
        return " ".join(letter if letter in self.guesses else "_" for letter in self.word)

    def guess(self, letter: str) -> "Hangman":
        """Aceita uma letra ASCII; rejeita palpites após o encerramento."""
        if self.finished:
            raise ValueError("Esta partida já terminou.")
        normalized = letter.strip().lower()
        if len(normalized) != 1 or normalized not in string.ascii_lowercase:
            raise ValueError("Digite apenas uma letra de a a z.")
        return Hangman(self.word, self.guesses | {normalized}, self.max_mistakes)
