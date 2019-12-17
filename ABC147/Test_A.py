import pytest
from A import solve


def test_solve():
    assert solve('5 7 9') == 'win'
    assert solve('13 7 2') == 'bust'
