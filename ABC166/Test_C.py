import pytest
from C import solve


def test_solve():
    assert solve('4 3\n1 2 3 4\n1 3\n2 3\n2 4') == '2'
    assert solve('6 5\n8 6 9 1 2 1\n1 3\n4 2\n4 3\n4 6\n4 6') == '3'
