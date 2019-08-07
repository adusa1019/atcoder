import pytest
from C import solve


def test_solve():
    assert solve('000') == '1'
    assert solve('10010010') == '3'
    assert solve('0') == '0'
