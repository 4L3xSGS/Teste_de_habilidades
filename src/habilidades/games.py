"""Aleatoriedade recreativa isolada; não deve ser usada para segredos."""

import random
from typing import Literal, Protocol

Coin = Literal["cara", "coroa"]
WORDS = ("python", "programa", "desenvolvedor", "computador", "algoritmo")


class RandomSource(Protocol):
    """Contrato mínimo que permite testes determinísticos sem afetar o RNG global."""

    def randint(self, a: int, b: int) -> int: ...


def flip_coin(rng: RandomSource | None = None) -> Coin:
    """Sorteia uma face com probabilidade igual."""
    source = rng if rng is not None else random.Random()
    return "cara" if source.randint(0, 1) == 0 else "coroa"


def roll_dice(
    count: int = 2, sides: int = 6, *, rng: RandomSource | None = None
) -> tuple[int, ...]:
    """Lança de 1 a 100 dados com 2 a 1000 faces cada."""
    if isinstance(count, bool) or not 1 <= count <= 100:
        raise ValueError("Use entre 1 e 100 dados.")
    if isinstance(sides, bool) or not 2 <= sides <= 1000:
        raise ValueError("Cada dado deve ter entre 2 e 1000 faces.")
    source = rng if rng is not None else random.Random()
    return tuple(source.randint(1, sides) for _ in range(count))


def choose_word(rng: RandomSource | None = None) -> str:
    """Escolhe uma palavra do catálogo educacional."""
    source = rng if rng is not None else random.Random()
    return WORDS[source.randint(0, len(WORDS) - 1)]
