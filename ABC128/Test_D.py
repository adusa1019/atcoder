import pytest
from D import solve


def test_solve():
    assert solve('7 3\n-10 -10 -10 31 -10 -10 -10') == '0'
    assert solve('7 4\n-10 -10 -10 31 -10 -10 -10') == '1'
    assert solve('7 4\n-9 -10 -10 31 -10 -10 -10') == '2'
    assert solve('7 4\n-10 -9 -10 31 -10 -10 -10') == '2'
    assert solve('7 4\n-10 -10 -9 31 -10 -10 -10') == '2'
    assert solve('7 4\n-10 -10 -10 31 -9 -10 -10') == '2'
    assert solve('7 4\n-10 -10 -10 31 -10 -9 -10') == '2'
    assert solve('7 4\n-10 -10 -10 31 -10 -10 -9') == '2'
    assert solve('7 5\n-10 -10 -10 31 -10 -10 -10') == '11'
    assert solve('7 5\n-9 -10 -10 31 -10 -10 -10') == '12'
    assert solve('7 6\n-10 -10 -10 31 -10 -10 -10') == '21'
    assert solve('7 6\n-9 -10 -10 31 -10 -10 -10') == '22'
    assert solve('7 7\n-10 -10 -10 31 -10 -10 -10') == '31'
    assert solve('6 20\n-6 -2 10 -8 2 -1') == '12'
    assert solve('6 11\n10 -8 -2 -1 -2 -6') == '10'
    assert solve('6 0\n-10 8 2 1 2 6') == '0'
    assert solve('6 4\n-10 8 2 1 2 6') == '14'
    assert solve('6 4\n-6 -100 50 -2 -5 -3') == '44'
    assert solve('6 3\n-6 -100 50 -2 -5 -3') == '0'
