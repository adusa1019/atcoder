import pytest
from C import solve


def test_solve():
    assert solve('3\n2 0\n3 1\n1 3\n4 2\n0 4\n5 5') == '2'
    assert solve('3\n0 0\n1 1\n5 2\n2 3\n3 4\n4 5') == '2'
    assert solve('2\n2 2\n3 3\n0 0\n1 1') == '0'
    assert solve('5\n0 0\n7 3\n2 2\n4 8\n1 6\n8 5\n6 9\n5 4\n9 1\n3 7') == '5'
    assert solve('5\n0 0\n1 1\n5 5\n6 6\n7 7\n2 2\n3 3\n4 4\n8 8\n9 9') == '4'
