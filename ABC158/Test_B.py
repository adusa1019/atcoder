import pytest
from B import solve


def test_solve():
    assert solve('8 3 4') == '4'
    assert solve('8 0 4') == '0'
    assert solve('6 2 4') == '2'
