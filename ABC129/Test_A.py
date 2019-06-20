import pytest
from A import solve


def test_solve():
    assert solve('1 3 4') == '4'
    assert solve('3 2 3') == '5'
