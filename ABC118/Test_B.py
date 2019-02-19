import pytest
from B import solve


def test_solve():
    assert solve('3 4\n2 1 3\n3 1 2 3\n2 3 2') == '1'
    assert solve('5 5\n4 2 3 4 5\n4 1 3 4 5\n4 1 2 4 5\n4 1 2 3 5\n4 1 2 3 4') == '0'
    assert solve('1 30\n3 5 10 30') == '3'
