import pytest
from B import solve


def test_solve():
    assert solve('1905') == 'YYMM'
    assert solve('0112') == 'AMBIGUOUS'
    assert solve('1700') == 'NA'
