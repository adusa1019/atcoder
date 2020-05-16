import pytest
from B import solve


def test_solve():
    assert solve('15') == '60'
    assert solve('1000000') == '266666333332'
