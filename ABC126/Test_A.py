import pytest
from A import solve


def test_solve():
    assert solve('3 1\nABC') == 'aBC'
    assert solve('4 3\nCABA') == 'CAbA'
