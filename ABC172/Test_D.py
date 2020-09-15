import pytest
from D import solve


def test_solve():
    assert solve('4') == '23'
    assert solve('100') == '26879'
    assert solve('10000000') == '838627288460105'
