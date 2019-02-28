import pytest
from B import solve


def test_solve():
    assert solve('2\n12 5\n1000 2000') == '1'
    assert solve('3\n21 -11\n81234 94124 52141') == '3'
