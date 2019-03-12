import pytest
from C import solve


def test_solve():
    assert solve('5\n2 2 3 5 5') == '2'
    assert solve('9\n1 2 3 4 5 6 7 8 9') == '0'
    assert solve('6\n6 5 4 3 2 1') == '18'
    assert solve('7\n1 1 1 1 2 3 4') == '6'
    assert solve('5\n1 2 3 4 10') == '5'
