import pytest
from D import solve


def test_solve():
    assert solve('2 6') == '4'
    assert solve('3 12') == '18'
    assert solve('100000 1000000000') == '957870001'
