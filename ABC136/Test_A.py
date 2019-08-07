import pytest
from A import solve


def test_solve():
    assert solve('6 4 3') == '1'
    assert solve('8 3 9') == '4'
    assert solve('12 3 7') == '0'
