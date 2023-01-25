from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    assert encrypt_message("teste", 2) == "ets_et"
    assert encrypt_message("teste2", 3) == "set_2et"
    assert encrypt_message("teste2", 7) == "2etset"
    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message("teste", "teste")
    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(1, 1)
