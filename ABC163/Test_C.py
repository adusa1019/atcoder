import pytest
from C import solve


def test_solve():
    assert solve('5\n1 1 2 2') == '2\n2\n0\n0\n0'
    assert solve('10\n1 1 1 1 1 1 1 1 1') == '9\n0\n0\n0\n0\n0\n0\n0\n0\n0'
    assert solve('7\n1 2 3 4 5 6') == '1\n1\n1\n1\n1\n1\n0'
