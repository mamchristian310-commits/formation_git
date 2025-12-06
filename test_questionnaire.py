import pytest
import builtins
from questionnaire import choose_file

def test_choose_file_valid(monkeypatch):
    monkeypatch.setattr(builtins, "input", lambda _: "cinema_alien_expert.json")
    assert choose_file() == "cinema_alien_expert.json"
    
