from challenges.challenge_encrypt_message import encrypt_message
import pytest

def test_encrypt_message():
    with pytest.raises(TypeError):
        encrypt_message(2, 'aaaaaa')
    with pytest.raises(TypeError):
        encrypt_message('aaaaaa', 'aaaaaa')
    with pytest.raises(TypeError):
        encrypt_message(2, 2)
    assert encrypt_message('UFF', 2) == 'F_FU'
    assert encrypt_message('RJ', 0) == 'JR'
    assert encrypt_message('Petrobras', 5) == 'orteP_sarb'
