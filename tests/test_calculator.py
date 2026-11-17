"""Contratos numéricos, entradas inválidas e estouro de operações."""

import pytest

from habilidades.calculator import calculate


@pytest.mark.parametrize(
    ("a", "b", "operation", "expected"),
    [(2, 3, "+", 5), (2, 3, "-", -1), (2, 3, "*", 6), (7, 2, "/", 3.5)],
)
def test_operations(a: float, b: float, operation: str, expected: float) -> None:
    assert calculate(a, b, operation) == expected


@pytest.mark.parametrize(
    ("a", "b", "operation"),
    [(1, 0, "/"), (1, 1, "%"), (float("nan"), 1, "+"), (1, float("inf"), "*"), (1e308, 1e308, "+")],
)
def test_rejects_invalid_arithmetic(a: float, b: float, operation: str) -> None:
    with pytest.raises(ValueError):
        calculate(a, b, operation)
