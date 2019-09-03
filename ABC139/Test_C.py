import pytest
from C import solve


def test_solve():
    assert solve('5\n10 4 8 7 3') == '2'
    assert solve('7\n4 4 5 6 6 5 5') == '3'
    assert solve('4\n1 2 3 4') == '0'
