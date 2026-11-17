"""Fonte aleatória injetável: sem testes estatísticos instáveis."""

import random

import pytest

from habilidades.games import WORDS, choose_word, flip_coin, roll_dice


def test_reproducible_dice_and_bounds() -> None:
    first = roll_dice(100, 20, rng=random.Random(42))
    assert first == roll_dice(100, 20, rng=random.Random(42))
    assert all(1 <= die <= 20 for die in first)
    assert len(first) == 100


@pytest.mark.parametrize(
    ("count", "sides"), [(0, 6), (101, 6), (2, 1), (2, 1001), (True, 6), (2, True)]
)
def test_dice_validation(count: int, sides: int) -> None:
    with pytest.raises(ValueError):
        roll_dice(count, sides)


class ExtremeRandom:
    def __init__(self, high: bool) -> None:
        self.high = high

    def randint(self, a: int, b: int) -> int:
        return b if self.high else a


@pytest.mark.parametrize(("high", "face"), [(False, "cara"), (True, "coroa")])
def test_coin_faces(high: bool, face: str) -> None:
    assert flip_coin(ExtremeRandom(high)) == face


def test_word_catalog() -> None:
    assert choose_word(ExtremeRandom(False)) == WORDS[0]
    assert choose_word(ExtremeRandom(True)) == WORDS[-1]
    assert choose_word() in WORDS
    assert flip_coin() in {"cara", "coroa"}
    assert len(roll_dice()) == 2
