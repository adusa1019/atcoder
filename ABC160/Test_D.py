import pytest
from D import solve


def test_solve():
    assert solve('5 2 4') == '5\n4\n1\n0'
    assert solve('3 1 3') == '3\n0'
    assert solve('7 3 7') == '7\n8\n4\n2\n0\n0'
    assert solve('10 4 8') == '10\n12\n10\n8\n4\n1\n0\n0\n0'
