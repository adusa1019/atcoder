import pytest
from C import solve


def test_solve():
    assert solve('35') == '1'
    assert solve('369') == '0'
    assert solve('6227384') == '1'
    assert solve('11') == '-1'
