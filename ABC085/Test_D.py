import pytest
from D import solve


def test_solve():
    assert solve('1 10\n3 5') == '3'
    assert solve('2 10\n3 5\n2 6') == '2'
    assert solve('4 1000000000\n1 1\n1 10000000\n1 30000000\n1 99999999') == '860000004'
    assert solve('5 500\n35 44\n28 83\n46 62\n31 79\n40 43') == '9'
