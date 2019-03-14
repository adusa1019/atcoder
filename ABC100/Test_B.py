import pytest
from B import solve


def test_solve():
    assert solve('0 5') == '5'
    assert solve('1 11') == '1100'
    assert solve('2 85') == '850000'
