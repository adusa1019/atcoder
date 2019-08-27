import pytest
from A import solve


def test_solve():
    assert solve('3 5') == '0'
    assert solve('7 5') == '10'
    assert solve('6 6') == '10'
