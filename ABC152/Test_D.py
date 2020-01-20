import pytest
from D import solve


def test_solve():
    assert solve('25') == '17'
    assert solve('1') == '1'
    assert solve('100') == '108'
    assert solve('2020') == '40812'
    assert solve('200000') == '400000008'
