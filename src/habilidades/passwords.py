"""Geração local de senhas usando a aleatoriedade do sistema operacional."""

import secrets
import string

MIN_LENGTH = 8
MAX_LENGTH = 1024


def generate_password(
    length: int = 16,
    *,
    uppercase: bool = True,
    digits: bool = True,
    symbols: bool = True,
) -> str:
    """Inclui ao menos um caractere de cada grupo habilitado, sem gravar a senha."""
    if isinstance(length, bool) or not MIN_LENGTH <= length <= MAX_LENGTH:
        raise ValueError(f"O tamanho deve estar entre {MIN_LENGTH} e {MAX_LENGTH}.")
    groups = [string.ascii_lowercase]
    if uppercase:
        groups.append(string.ascii_uppercase)
    if digits:
        groups.append(string.digits)
    if symbols:
        groups.append(string.punctuation)
    alphabet = "".join(groups)
    characters = [secrets.choice(group) for group in groups]
    characters.extend(secrets.choice(alphabet) for _ in range(length - len(groups)))
    # Fisher–Yates com randbelow, sem random.shuffle ou previsibilidade de PRNG.
    for index in range(len(characters) - 1, 0, -1):
        target = secrets.randbelow(index + 1)
        characters[index], characters[target] = characters[target], characters[index]
    return "".join(characters)
