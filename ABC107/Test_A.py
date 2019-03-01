import pytest
from A import solve


def test_solve():
    assert solve('4 2') == '3'
    assert solve('1 1') == '1'
    assert solve('15 11') == '5'
