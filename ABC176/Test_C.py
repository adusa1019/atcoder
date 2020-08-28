import pytest
from C import solve


def test_solve():
    assert solve('5\n2 1 5 4 3') == '4'
    assert solve('5\n3 3 3 3 3') == '0'
