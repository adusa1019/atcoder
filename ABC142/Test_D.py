import pytest
from D import solve


def test_solve():
    assert solve('2 2') == '2'
    assert solve('5 5') == '2'
    assert solve('12 18') == '3'
    assert solve('22 22') == '3'
    assert solve('420 660') == '4'
    assert solve('1 2019') == '1'
    assert solve('30030 30030') == '7'
    assert solve('1000000000000 1000000000000') == '3'
