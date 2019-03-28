import pytest
from A import solve


def test_solve():
    assert solve('3 8 7 1') == 'Left'
    assert solve('3 4 5 2') == 'Balanced'
    assert solve('1 7 6 4') == 'Right'
