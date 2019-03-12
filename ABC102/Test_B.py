import pytest
from B import solve


def test_solve():
    assert solve('4\n1 4 6 3') == '5'
    assert solve('2\n1000000000 1') == '999999999'
    assert solve('5\n1 1 1 1 1') == '0'
