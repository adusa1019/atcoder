import pytest
from A import solve


def test_solve():
    assert solve('4') == '0.5'
    assert solve('5') == '0.6'
    assert solve('1') == '1.0'
