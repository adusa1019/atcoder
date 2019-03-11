import pytest
from A import solve


def test_solve():
    assert solve('1 6 3') == '5'
    assert solve('11 5 5') == '6'
    assert solve('100 100 100') == '0'
