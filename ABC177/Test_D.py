import pytest
from D import solve


def test_solve():
    assert solve('5 3\n1 2\n3 4\n5 1') == '3'
    assert solve('4 10\n1 2\n2 1\n1 2\n2 1\n1 2\n1 3\n1 4\n2 3\n2 4\n3 4') == '4'
    assert solve('10 4\n3 1\n4 1\n5 9\n2 6') == '3'
