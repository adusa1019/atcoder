import pytest
from D import solve


def test_solve():
    assert solve('3 3\n2 13 8') == '9'
    assert solve('4 4\n1 9 3 5') == '6'
    assert solve('1 100000\n1000000000') == '0'
    assert solve('10 1\n1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000') == '9500000000'
