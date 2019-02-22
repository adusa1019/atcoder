import pytest
from C import solve


def test_solve():
    # assert solve('2 5\n10 12 1 2 14') == '5'
    # assert solve('3 7\n-10 -3 0 9 -100 2 17') == '19'
    # assert solve('100 1\n-100000') == '0'
    assert solve('1 2\n-100000 0') == '100000'
