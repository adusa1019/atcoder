import pytest
from A import solve


def test_solve():
    assert solve('5 3') == '9'
    assert solve('3 4') == '7'
    assert solve('6 6') == '12'
