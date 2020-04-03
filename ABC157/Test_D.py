import pytest
from D import solve


def test_solve():
    assert solve('4 4 1\n2 1\n1 3\n3 2\n3 4\n4 1') == '0 1 0 1'
    assert solve('5 10 0\n1 2\n1 3\n1 4\n1 5\n3 2\n2 4\n2 5\n4 3\n5 3\n4 5') == '0 0 0 0 0'
    assert solve('10 9 3\n10 1\n6 7\n8 2\n2 5\n8 4\n7 3\n10 9\n6 4\n5 8\n2 6\n7 5\n3 1') == '1 3 5 4 3 3 3 3 1 0'
