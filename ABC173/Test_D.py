import pytest
from D import solve


def test_solve():
    assert solve('4\n2 2 1 3') == '7'
    assert solve('7\n1 1 1 1 1 1 1') == '6'
