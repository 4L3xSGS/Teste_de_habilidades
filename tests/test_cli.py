"""CLI com saída JSON, erros acionáveis e cancelamento previsível."""

import importlib
import json
import subprocess
import sys
from collections.abc import Iterator

import pytest

from habilidades.cli import main


def test_calculator_json(capsys: pytest.CaptureFixture[str]) -> None:
    assert main(["calcular", "7", "/", "2", "--json"]) == 0
    assert json.loads(capsys.readouterr().out) == {"resultado": 3.5}


def test_invalid_operation_returns_error(capsys: pytest.CaptureFixture[str]) -> None:
    assert main(["calcular", "1", "/", "0"]) == 2
    captured = capsys.readouterr()
    assert not captured.out
    assert "zero" in captured.err


@pytest.mark.parametrize("choice", ["cara", "coroa"])
def test_coin_json(
    choice: str, capsys: pytest.CaptureFixture[str], monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr("habilidades.cli.flip_coin", lambda: "cara")
    assert main(["moeda", "--escolha", choice, "--json"]) == 0
    assert json.loads(capsys.readouterr().out)["acertou"] is (choice == "cara")


def test_dice_json(capsys: pytest.CaptureFixture[str]) -> None:
    assert main(["dados", "--quantidade", "4", "--faces", "20", "--json"]) == 0
    data = json.loads(capsys.readouterr().out)
    assert len(data["dados"]) == 4 and data["soma"] == sum(data["dados"])


def test_password_json(capsys: pytest.CaptureFixture[str]) -> None:
    assert main(["senha", "--tamanho", "24", "--sem-simbolos", "--json"]) == 0
    assert len(json.loads(capsys.readouterr().out)["senha"]) == 24


@pytest.mark.parametrize("args", [["calcular", "3", "+", "2"], ["moeda"], ["dados"], ["senha"]])
def test_text_output(args: list[str], capsys: pytest.CaptureFixture[str]) -> None:
    assert main(args) == 0
    assert capsys.readouterr().out.strip()


@pytest.mark.parametrize("args", [["dados", "--quantidade", "0"], ["senha", "--tamanho", "0"]])
def test_invalid_limits(args: list[str], capsys: pytest.CaptureFixture[str]) -> None:
    assert main(args) == 2
    assert "Erro:" in capsys.readouterr().err


@pytest.mark.parametrize("args", [[], ["calcular", "x", "+", "2"], ["moeda", "--escolha", "borda"]])
def test_argparse_rejects_bad_usage(args: list[str]) -> None:
    with pytest.raises(SystemExit) as error:
        main(args)
    assert error.value.code == 2


def test_hangman_interaction(
    monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    monkeypatch.setattr("habilidades.cli.choose_word", lambda: "ab")
    answers: Iterator[str] = iter(["12", "a", "a", "b"])
    monkeypatch.setattr("builtins.input", lambda _: next(answers))
    assert main(["forca"]) == 0
    text = capsys.readouterr().out
    assert "Você venceu!" in text and "já tentou" in text and "letra de a a z" in text


@pytest.mark.parametrize("exception", [EOFError, KeyboardInterrupt])
def test_interruption(exception: type[BaseException], monkeypatch: pytest.MonkeyPatch) -> None:
    def interrupt(_: str) -> str:
        raise exception

    monkeypatch.setattr("builtins.input", interrupt)
    assert main(["forca"]) == 130


def test_module_entrypoint() -> None:
    completed = subprocess.run(
        [sys.executable, "-m", "habilidades", "calcular", "2", "+", "3", "--json"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert json.loads(completed.stdout) == {"resultado": 5.0}


def test_legacy_imports_have_no_side_effects(
    monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    monkeypatch.syspath_prepend(".")
    for module in ("calculadora2", "cara_coroa", "forca", "gerador_senhas", "jogo_dados"):
        importlib.import_module(module)
    assert capsys.readouterr().out == ""
