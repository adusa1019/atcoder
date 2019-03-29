import pytest
from C import solve


def test_solve():
    assert solve('2 5\n4 9\n2 4') == '12'
    assert solve('4 30\n6 18\n2 5\n3 10\n7 9') == '130'
    assert solve('1 100000\n1000000000 100000') == '100000000000000'
