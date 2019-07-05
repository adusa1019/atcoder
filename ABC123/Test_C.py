import pytest
from C import solve


def test_solve():
    assert solve('5\n3\n2\n4\n3\n5') == '7'
    assert solve('10\n123\n123\n123\n123\n123') == '5'
    assert solve('10000000007\n2\n3\n5\n7\n11') == '5000000008'
