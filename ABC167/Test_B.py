import pytest
from B import solve


def test_solve():
    assert solve('2 1 1 3') == '2'
    assert solve('1 2 3 4') == '0'
    assert solve('2000000000 0 0 2000000000') == '2000000000'
