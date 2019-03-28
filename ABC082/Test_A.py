import pytest
from A import solve


def test_solve():
    assert solve('1 3') == '2'
    assert solve('7 4') == '6'
    assert solve('5 5') == '5'
