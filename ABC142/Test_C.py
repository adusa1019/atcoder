import pytest
from C import solve


def test_solve():
    assert solve('3\n2 3 1') == '3 1 2'
    assert solve('5\n1 2 3 4 5') == '1 2 3 4 5'
    assert solve('8\n8 2 7 3 4 5 6 1') == '8 2 4 5 6 7 3 1'
