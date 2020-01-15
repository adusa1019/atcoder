import pytest
from D import solve


def test_solve():
    assert solve('2 50\n6 10') == '2'
    assert solve('2 100\n14 22') == '1'
    assert solve('3 100\n14 22 40') == '0'
    assert solve('5 1000000000\n6 6 2 6 2') == '166666667'
