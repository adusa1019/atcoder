import pytest
from D import solve


def test_solve():
    assert solve('15') == '23'
    assert solve('1') == '1'
    assert solve('13') == '21'
    assert solve('100000') == '3234566667'
