import pytest
# from D import solve
from D_1 import solve


def test_solve():
    assert solve('3') == '61'
    assert solve('4') == '230'
    assert solve('5') == '865'
    assert solve('6') == '3247'
    assert solve('7') == '12185'
    assert solve('8') == '45719'
    assert solve('9') == '171531'
    assert solve('100') == '388130742'
