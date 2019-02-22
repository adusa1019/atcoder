import pytest
from C import solve


def test_solve():
    assert solve('4\n1 2 2 1') == '2'
    assert solve('5\n3 1 2 3 1') == '5'
    assert solve('8\n4 23 75 0 23 96 50 100') == '221'
