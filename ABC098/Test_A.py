import pytest
from A import solve


def test_solve():
    assert solve('3 1') == '4'
    assert solve('4 -2') == '6'
    assert solve('0 0') == '0'
