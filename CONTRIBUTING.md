# Contribuir

1. Crie uma branch com um objetivo pequeno e observável.
2. Execute `uv sync --locked` para preparar o ambiente.
3. Separe regras de apresentação e adicione casos de teste que representem o comportamento alterado.
4. Execute `uv run ruff check .`, `uv run ruff format --check .`, `uv run mypy`, `uv run pytest` e `uv build`.
5. Abra um pull request explicando o problema, o resultado e a validação.

Para atualizar ferramentas, altere as dependências e gere novamente `uv.lock` com `uv lock`. Evite atualizar pacotes sem relação com a mudança. Não inclua senhas, dados pessoais ou arquivos de ambientes virtuais nos commits.

Mudanças nas entradas históricas devem declarar o impacto de compatibilidade. Novas funcionalidades da CLI devem documentar entrada, saída, erros e limites. O pacote não deve realizar I/O ao ser importado.
