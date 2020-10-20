import pytest
from B import solve


def test_solve():
    assert solve('1 2 1 1') == '2'
    assert solve('3 5 -4 -2') == '-6'
    assert solve('-1000000000 0 -1000000000 0') == '1000000000000000000'
