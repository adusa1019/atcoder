import pytest
from C import solve


def test_solve():
    assert solve('4\n3 3 3 3') == '1'
    assert solve('5\n2 4 1 4 2') == '2'
    assert solve('6\n1 2 2 3 3 3') == '0'
    assert solve('1\n1000000000') == '1'
    assert solve('8\n2 7 1 8 2 8 1 8') == '5'
