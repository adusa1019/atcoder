import pytest
from C import solve


def test_solve():
    assert solve('4 330\n0 1 10 100\n1 0 20 200\n10 20 0 300\n100 200 300 0') == '2'
    assert solve('5 5\n0 1 1 1 1\n1 0 1 1 1\n1 1 0 1 1\n1 1 1 0 1\n1 1 1 1 0') == '24'
