import pytest
from D import solve


def test_solve():
    assert solve('3 14') == '2'
    assert solve('10 123') == '3'
    assert solve('100000 1000000000') == '10000'
