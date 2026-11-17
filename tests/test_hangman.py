"""Transições de estado e limites de tentativas."""

import pytest

from habilidades.hangman import Hangman


def test_correct_repeated_and_wrong_guesses() -> None:
    original = Hangman("banana")
    game = original.guess(" A ")
    assert original.masked == "_ _ _ _ _ _"
    assert game.masked == "_ a _ a _ a"
    assert game.remaining == 6
    game = game.guess("x")
    assert game.remaining == 5
    assert game.guess("x") == game


def test_win_and_no_moves_after_end() -> None:
    game = Hangman("a").guess("a")
    assert game.won and game.finished
    with pytest.raises(ValueError, match="terminou"):
        game.guess("b")


def test_loss() -> None:
    game = Hangman("a", max_mistakes=1).guess("b")
    assert game.finished and not game.won and game.remaining == 0


@pytest.mark.parametrize("letter", ["", "ab", "1", "é", "!"])
def test_invalid_guesses(letter: str) -> None:
    with pytest.raises(ValueError):
        Hangman("python").guess(letter)


@pytest.mark.parametrize("word", ["", "Python", "dois termos", "ação"])
def test_invalid_words(word: str) -> None:
    with pytest.raises(ValueError):
        Hangman(word)


def test_invalid_state() -> None:
    with pytest.raises(ValueError):
        Hangman("a", max_mistakes=0)
    with pytest.raises(ValueError):
        Hangman("a", guesses=frozenset({"ab"}))
