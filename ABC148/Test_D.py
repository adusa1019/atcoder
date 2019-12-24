import pytest
from D import solve


def test_solve():
    assert solve('3\n2 1 2') == '1'
    assert solve('3\n2 2 2') == '-1'
    assert solve('10\n3 1 4 1 5 9 2 6 5 3') == '7'
    assert solve('1\n1') == '0'
