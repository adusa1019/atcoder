import pytest
from D import solve


def test_solve():
    assert solve('RRLRL') == '0 1 2 1 1'
    assert solve('RRLLLLRLRRLL') == '0 3 3 0 0 0 1 1 0 2 2 0'
    assert solve('RRRLLRLLRRRLLLLL') == '0 0 3 2 0 2 1 0 0 0 4 4 0 0 0 0'