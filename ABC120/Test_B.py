import pytest
from B import solve


def test_solve():
    assert solve('8 12 2') == '2'
    assert solve('100 50 4') == '5'
    assert solve('1 1 1') == '1'
