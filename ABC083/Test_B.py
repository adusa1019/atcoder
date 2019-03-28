import pytest
from B import solve


def test_solve():
    assert solve('20 2 5') == '84'
    assert solve('10 1 2') == '13'
    assert solve('100 4 16') == '4554'
