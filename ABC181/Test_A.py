import pytest
from A import solve


def test_solve():
    assert solve('2') == 'White'
    assert solve('5') == 'Black'
