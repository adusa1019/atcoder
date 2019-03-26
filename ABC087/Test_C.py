import pytest
from C import solve


def test_solve():
    assert solve('5\n3 2 2 4 1\n1 2 2 2 1') == '14'
    assert solve('4\n1 1 1 1\n1 1 1 1') == '5'
    assert solve('4\n1 1 1 1\n0 0 0 1') == '5'
    assert solve('7\n3 3 4 5 4 5 3\n5 3 4 4 2 3 2') == '29'
    assert solve('1\n2\n3') == '5'
