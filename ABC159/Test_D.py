import pytest
from D import solve


def test_solve():
    assert solve('5\n1 1 2 1 2') == '2\n2\n3\n2\n3'
    assert solve('4\n1 2 3 4') == '0\n0\n0\n0'
    assert solve('5\n3 3 3 3 3') == '6\n6\n6\n6\n6'
    assert solve('8\n1 2 1 4 2 1 4 1') == '5\n7\n5\n7\n7\n5\n7\n5'
