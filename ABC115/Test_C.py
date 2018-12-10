import pytest
from C import solve


def test_solve():
    assert solve('5 3\n10\n15\n11\n14\n12') == '2'
    assert solve('5 3\n5\n7\n5\n7\n7') == '0'
