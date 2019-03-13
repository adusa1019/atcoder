import pytest
from C import solve


def test_solve():
    assert solve('4 3\n2 3 1 4') == '2'
    assert solve('3 3\n1 2 3') == '1'
    assert solve('8 3\n7 3 1 8 4 6 2 5') == '4'
    assert solve('10 3\n7 3 8 4 1 6 2 5 9 10') == '5'
