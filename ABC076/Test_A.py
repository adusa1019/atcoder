import pytest
from A import solve


def test_solve():
    assert solve('2002\n2017') == '2032'
    assert solve('4500\n0') == '-4500'
