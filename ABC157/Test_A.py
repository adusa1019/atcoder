import pytest
from A import solve


def test_solve():
    assert solve('5') == '3'
    assert solve('2') == '1'
    assert solve('100') == '50'
