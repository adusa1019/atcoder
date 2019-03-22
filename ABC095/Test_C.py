import pytest
from C import solve


def test_solve():
    assert solve('1500 2000 1600 3 2') == '7900'
    assert solve('2000 1500 1600 2 3') == '7900'
    assert solve('3000 1500 1400 3 2') == '8400'

    assert solve('1500 2000 1900 3 2') == '8500'
    assert solve('1500 2000 500 90000 100000') == '100000000'
