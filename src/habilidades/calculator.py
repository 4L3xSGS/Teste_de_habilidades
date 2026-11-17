"""Operações aritméticas com validação e resultados numéricos consistentes."""

import math
from typing import Literal

Operation = Literal["+", "-", "*", "/"]


def calculate(a: float, b: float, operation: str) -> float:
    """Calcula uma operação; rejeita valores não finitos e divisão por zero."""
    if not math.isfinite(a) or not math.isfinite(b):
        raise ValueError("Os números precisam ser finitos.")
    match operation:
        case "+":
            result = a + b
        case "-":
            result = a - b
        case "*":
            result = a * b
        case "/":
            if b == 0:
                raise ValueError("Não é possível dividir por zero.")
            result = a / b
        case _:
            raise ValueError("Operação inválida. Use +, -, * ou /.")
    if not math.isfinite(result):
        raise ValueError("O resultado ultrapassa o intervalo numérico suportado.")
    return result
