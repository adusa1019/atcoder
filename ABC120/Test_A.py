import pytest
from A import solve


def test_solve():
    assert solve('2 11 4') == '4'
    assert solve('3 9 5') == '3'
    assert solve('100 1 10') == '0'
