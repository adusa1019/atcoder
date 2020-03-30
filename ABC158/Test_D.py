import pytest
from D import solve


def test_solve():
    assert solve('a\n4\n2 1 p\n1\n2 2 c\n1') == 'cpa'
    assert solve('a\n6\n2 2 a\n2 1 b\n1\n2 2 c\n1\n1') == 'aabc'
    assert solve('y\n1\n2 1 x') == 'xy'
