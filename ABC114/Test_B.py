import pytest
from B import solve


def test_solve():
    assert solve('1234567876') == '34'
    assert solve('35753') == '0'
    assert solve('1111111111') == '642'
