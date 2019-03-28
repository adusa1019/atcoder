import pytest
from D import solve


def test_solve():
    assert solve('010') == '2'
    assert solve('100000000') == '8'
    assert solve('00001111') == '4'
