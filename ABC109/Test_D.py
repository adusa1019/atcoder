import pytest
from D import solve


def test_solve():
    assert solve('2 3\n1 2 3\n0 1 1') == '3\n1 1 1 2\n1 2 1 3\n2 2 2 3'
    assert solve('3 2\n1 0\n2 1\n1 0') == '3\n1 1 1 2\n1 2 2 2\n3 1 3 2'
    assert solve('1 5\n9 9 9 9 9') == '2\n1 1 1 2\n1 3 1 4'
