import pytest
from A import solve


def test_solve():
    assert solve('SAT') == '1'
    assert solve('SUN') == '7'
