import pytest
from A import solve


def test_solve():
    assert solve('5 5') == '5'
    assert solve('2 1') == '1'
    assert solve('11 30') == '11'
