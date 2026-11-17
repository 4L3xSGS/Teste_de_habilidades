"""Políticas de caracteres verificadas, sem registrar senhas em snapshots."""

import itertools
import string

import pytest

from habilidades.passwords import generate_password


@pytest.mark.parametrize(
    ("uppercase", "digits", "symbols"), list(itertools.product([False, True], repeat=3))
)
def test_password_groups(uppercase: bool, digits: bool, symbols: bool) -> None:
    password = generate_password(32, uppercase=uppercase, digits=digits, symbols=symbols)
    assert len(password) == 32
    assert any(c in string.ascii_lowercase for c in password)
    for enabled, group in [
        (uppercase, string.ascii_uppercase),
        (digits, string.digits),
        (symbols, string.punctuation),
    ]:
        assert any(c in group for c in password) is enabled


@pytest.mark.parametrize("length", [-1, 0, 7, 1025, True])
def test_rejects_invalid_length(length: int) -> None:
    with pytest.raises(ValueError):
        generate_password(length)


@pytest.mark.parametrize("length", [8, 1024])
def test_length_boundaries(length: int) -> None:
    assert len(generate_password(length)) == length
