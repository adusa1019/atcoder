import pytest
from B import solve


def test_solve():
    assert solve('13 3 1') == '3'
    assert solve('12 3 1') == '2'
    assert solve('100000 1 1') == '49999'
    assert solve('64146 123 456') == '110'
    assert solve('64145 123 456') == '109'
