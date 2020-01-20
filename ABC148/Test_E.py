import pytest
from E import solve


def test_solve():
    assert solve('12') == '1'
    assert solve('5') == '0'
    assert solve('18') == '1'
    assert solve('50') == '6'
    assert solve('100') == '12'
    assert solve('1000000000000000000') == '124999999999999995'
