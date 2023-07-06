from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():

    assert encrypt_message("testando", 3) == "set_odnat"

    assert encrypt_message("testando", 5) == "atset_odn"

    assert encrypt_message("testando", 4) == "odna_tset"

    assert encrypt_message("testando", 6) == "od_natset"

    assert encrypt_message("testando", 0) == "odnatset"

    assert encrypt_message("testando", -2) == "odnatset"

    assert encrypt_message("testando", 10) == "odnatset"

    assert encrypt_message("", 3) == ""

    with pytest.raises(TypeError):
        encrypt_message(3, "testando")

    with pytest.raises(TypeError):
        encrypt_message("testando", "xuxa")
