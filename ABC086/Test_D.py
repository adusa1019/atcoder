import pytest
from D import solve


def test_solve():
    assert solve('4 3\n0 1 W\n1 2 W\n5 3 B\n5 4 B') == '4'
    assert solve('2 1000\n0 0 B\n0 1 W') == '2'
    assert solve('6 2\n1 2 B\n2 1 W\n2 2 B\n1 0 B\n0 6 W\n4 5 W') == '4'
