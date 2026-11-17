# Decisões de engenharia

## Limite do projeto

Cinco exercícios educacionais se tornam um pacote de terminal. Os scripts originais permanecem como entradas de compatibilidade. A interface pública principal é `habilidades`; importar módulos não realiza I/O.

## Responsabilidades

| Camada | Arquivos | Contrato |
| --- | --- | --- |
| Entrada | `cli.py`, `__main__.py` | Interpreta argumentos, apresenta texto/JSON e escolhe código de saída |
| Regras | `calculator.py`, `passwords.py`, `hangman.py` | Resultados tipados e `ValueError` para domínio inválido |
| Sorteios recreativos | `games.py` | Usa fonte aleatória substituível por um objeto com `randint` |
| Compatibilidade | Scripts na raiz | Reaproveita o pacote preservando nomes e execução direta após instalação |

## Escolhas e consequências

1. **Biblioteca padrão em produção.** `argparse`, `dataclasses` e `secrets` cobrem o escopo. Não há framework de CLI ou servidor para manter. A interface é de terminal; não existe interface gráfica.
2. **Layout `src`.** A importação exige o pacote instalado. Isso permite que os testes e o uso comum validem a distribuição, sem depender da pasta raiz como pacote implícito.
3. **Estado imutável na forca.** Um palpite devolve um novo estado. É possível verificar vitória, derrota e repetição sem simular uma sessão de terminal. O vocabulário usa apenas a–z, e a entrada deixa essa restrição explícita.
4. **Duas classes de aleatoriedade.** Jogos usam `random` com protocolo injetável; senhas usam `secrets`. A regra Ruff S311 é dispensada somente no módulo recreativo e em testes.
5. **Grupos obrigatórios nas senhas.** Seleciona um caractere de cada grupo habilitado, preenche o restante e embaralha com Fisher–Yates e `secrets.randbelow`. O resultado cumpre a política, mas a distribuição não é uniforme sobre todas as strings possíveis que cumprem a política; não se anuncia uma medida de entropia não demonstrada.
6. **Calculadora com float.** Adequada aos exercícios; não é uma calculadora financeira. Aritmética monetária exigiria `Decimal` e regras próprias de arredondamento.
7. **uv com lockfile.** O mesmo conjunto resolvido é usado localmente e em CI. Requisitos em `pyproject.toml` descrevem faixas; `uv.lock` fixa a resolução. O backend de build tem seu próprio intervalo de versão e é resolvido em isolamento.
8. **Testes com casos de domínio.** Falhas numéricas, limites, presença/ausência de grupos, repetição de letras, interrupção e saída estruturada. A matriz Linux/Windows verifica a instalação e a execução, não só funções isoladas.

## Mudanças de compatibilidade intencionais

- Divisão por zero passa a lançar `ValueError` nas funções; a CLI apresenta mensagem e retorna 2.
- Senhas com menos de 8 ou mais de 1.024 caracteres são recusadas.
- Nenhum script executa interações ao ser importado.
- A execução dos scripts da raiz requer ambiente com o pacote instalado (`uv run` prepara esse ambiente).

## Critério para novas dependências

Adicionar uma dependência somente quando houver problema reproduzível ou recurso solicitado que a biblioteca padrão não atenda com clareza. Docker, serviços externos e IA não são necessários para operar este laboratório.

Referências: [uv](https://docs.astral.sh/uv/), [Ruff](https://docs.astral.sh/ruff/), [pytest](https://docs.pytest.org/), [mypy](https://mypy.readthedocs.io/), [secrets](https://docs.python.org/3/library/secrets.html).
