import pytest
from B import solve


def test_solve():
    assert solve('2\n1 3\n3 5') == '18'
    assert solve('3\n11 13\n17 47\n359 44683') == '998244353'
    assert solve('1\n1 1000000') == '500000500000'
