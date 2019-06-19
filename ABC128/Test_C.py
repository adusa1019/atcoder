import pytest
from C import solve


def test_solve():
    assert solve('2 2\n2 1 2\n1 2\n0 1') == '1'
    assert solve('2 3\n2 1 2\n1 1\n1 2\n0 0 1') == '0'
    assert solve('5 2\n3 1 2 5\n2 2 3\n1 0') == '8'
