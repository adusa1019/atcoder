import pytest
from D import solve


def test_solve():
    assert solve('3\n2 2 4') == '4 0 4'
    assert solve('5\n3 8 7 5 5') == '2 4 12 2 8'
    assert solve('3\n1000000000 1000000000 0') == '0 2000000000 0'
