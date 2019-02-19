import pytest
from C import solve


def test_solve():
    assert solve('4\n2 10 8 40') == '2'
    assert solve('4\n5 13 8 1000000000') == '1'
    assert solve('3\n1000000000 1000000000 1000000000') == '1000000000'
