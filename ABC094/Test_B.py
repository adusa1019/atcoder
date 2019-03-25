import pytest
from B import solve


def test_solve():
    assert solve('5 3 3\n1 2 4') == '1'
    assert solve('7 3 2\n4 5 6') == '0'
    assert solve('10 7 5\n1 2 3 4 6 8 9') == '3'
