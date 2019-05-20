import pytest
from D import solve


def test_solve():
    assert solve('3\n1 2 2\n2 3 1') == '0\n0\n1'
    assert solve('5\n2 5 2\n2 3 10\n1 3 8\n3 4 2') == '0\n0\n0\n0\n0'
