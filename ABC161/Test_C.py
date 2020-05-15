import pytest
from C import solve


def test_solve():
    assert solve('7 4') == '1'
    assert solve('2 6') == '2'
    assert solve('1000000000000000000 1') == '0'
