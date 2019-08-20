import pytest
from B import solve


def test_solve():
    assert solve('2\n10 30') == '7.5'
    assert solve('3\n200 200 200') == '66.66666666666667'
    assert solve('1\n1000') == '1000.0'
