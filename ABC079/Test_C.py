import pytest
from C import solve


def test_solve():
    assert solve('1222') == '1+2+2+2=7'
    assert solve('0290') == '0-2+9+0=7'
    assert solve('3242') == '3+2+4-2=7'
