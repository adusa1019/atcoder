import pytest
from C import solve


def test_solve():
    assert solve('4 2\n1 3\n2 4') == '2'
    assert solve('10 3\n3 6\n5 7\n6 9') == '1'
    assert solve('100000 1\n1 100000') == '100000'
