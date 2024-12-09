import pytest

from authenticate import login, load_people

def test_login(capsys, monkeypatch):
    inputs = ['falsches']
    monkeypatch.setattr('builtins.input', lambda x: inputs.pop())
    login()
    captured = capsys.readouterr()
    assert captured.out == 'Passwort falsch'
