import pytest
from A import solve


def test_solve():
    assert solve('4 12') == '16'
    assert solve('8 20') == '12'
    assert solve('1 1') == '2'
