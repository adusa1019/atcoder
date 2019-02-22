import pytest
from A import solve


def test_solve():
    assert solve('3 4 5') == '6'
    assert solve('5 12 13') == '30'
    assert solve('45 28 53') == '630'
