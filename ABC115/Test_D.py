import pytest
from D import solve


def test_solve():
    assert solve('2 9') == '5'
    assert solve('2 8') == '4'
    assert solve('2 7') == '4'
    assert solve('1 1') == '0'
    assert solve('50 4321098765432109') == '2160549382716056'
