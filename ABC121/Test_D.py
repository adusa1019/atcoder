import pytest
from D import solve


def test_solve():
    assert solve('2 11') == '1'
    assert solve('2 10') == '10'
    assert solve('2 4') == '5'
    assert solve('123 456') == '435'
    assert solve('123456789012 123456789012') == '123456789012'
    assert solve('0 0') == '0'
