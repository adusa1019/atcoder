import pytest
from E import solve


def test_solve():
    # assert solve('5 3') == '5\n4 3\n1 2\n3 1\n4 5\n2 3'
    assert solve('5 8') == '-1'
