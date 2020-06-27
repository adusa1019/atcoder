import pytest
from D import solve


def test_solve():
    assert solve('24') == '3'
    assert solve('1') == '0'
    assert solve('6') == '2'
    assert solve('64') == '3'
    assert solve('1000000007') == '1'
    assert solve('997764507000') == '7'
