"""Compatibilidade com a função gerar_senha; geração segura no pacote habilidades."""

from habilidades.passwords import generate_password


def gerar_senha(
    tamanho: int = 12,
    usar_maiusculas: bool = True,
    usar_numeros: bool = True,
    usar_simbolos: bool = True,
) -> str:
    return generate_password(
        tamanho,
        uppercase=usar_maiusculas,
        digits=usar_numeros,
        symbols=usar_simbolos,
    )


if __name__ == "__main__":
    print(gerar_senha(tamanho=16))
