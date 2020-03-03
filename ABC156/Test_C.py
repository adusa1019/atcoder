import pytest
from C import solve


def test_solve():
    assert solve('2\n1 4') == '5'
    assert solve('7\n14 14 2 13 56 2 37') == '2354'
