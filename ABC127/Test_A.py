import pytest
from A import solve


def test_solve():
    assert solve('30 100') == '100'
    assert solve('12 100') == '50'
    assert solve('0 100') == '0'
