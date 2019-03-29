import pytest
from A import solve


def test_solve():
    assert solve('3 2\n2 1') == '1'
    assert solve('5 5\n2 3') == '6'
    assert solve('2 4\n2 4') == '0'
