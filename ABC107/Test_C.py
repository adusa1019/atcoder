import pytest
from C import solve


def test_solve():
    assert solve('5 3\n-30 -10 10 20 50') == '40'
    assert solve('3 2\n10 20 30') == '20'
    assert solve('1 1\n0') == '0'
    assert solve('8 5\n-9 -7 -4 -3 1 2 3 4') == '10'
