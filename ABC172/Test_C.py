import pytest
from C import solve


def test_solve():
    assert solve('3 4 240\n60 90 120\n80 150 80 150') == '3'
    assert solve('3 4 730\n60 90 120\n80 150 80 150') == '7'
    assert solve('5 4 1\n1000000000 1000000000 1000000000 1000000000 1000000000\n1000000000 1000000000 1000000000 1000000000') == '0'