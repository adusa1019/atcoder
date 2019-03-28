import pytest
from C import solve


def test_solve():
    assert solve('3 20') == '3'
    assert solve('25 100') == '3'
    assert solve('314159265 358979323846264338') == '31'
