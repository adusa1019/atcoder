import pytest
from D import solve


def test_solve():
    assert solve('5 3\n1 2 2 4 5') == '7.0'
    assert solve('4 1\n6 6 6 6') == '3.5'
    assert solve('4 4\n6 6 6 6') == '14.0'
    assert solve('10 4\n17 13 13 12 15 20 10 13 17 11') == '32.0'
