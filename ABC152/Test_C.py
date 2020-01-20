import pytest
from C import solve


def test_solve():
    assert solve('5\n4 2 5 1 3') == '3'
    assert solve('4\n4 3 2 1') == '4'
    assert solve('6\n1 2 3 4 5 6') == '1'
    assert solve('8\n5 7 4 2 6 8 1 3') == '4'
    assert solve('1\n1') == '1'
