import pytest
from B import solve


def test_solve():
    assert solve('2\nip cc') == 'icpc'
    assert solve('8\nhmhmnknk uuuuuuuu') == 'humuhumunukunuku'
    assert solve('5\naaaaa aaaaa') == 'aaaaaaaaaa'
