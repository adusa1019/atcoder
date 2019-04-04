import pytest
from B import solve


def test_solve():
    assert solve('10') == '9'
    assert solve('81') == '81'
    assert solve('271828182') == '271821169'
