import pytest
from D import solve


def test_solve():
    assert solve('1\n1') == '1'
    assert solve('2\n1 -2') == '2'
    assert solve('3\n1 -2 4') == '3'
    assert solve('3\n2 -1 -2') == '5'
    assert solve('5\n-2 1 3 -1 -1') == '2'
    assert solve('5\n-1000 -1000 -1000 -1000 -1000') == '0'
