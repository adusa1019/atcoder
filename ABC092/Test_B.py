import pytest
from B import solve


def test_solve():
    assert solve('3\n7 1\n2\n5\n10') == '8'
    assert solve('2\n8 20\n1\n10') == '29'
    assert solve('5\n30 44\n26\n18\n81\n18\n6') == '56'
