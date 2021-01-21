import pytest
from D import solve


def test_solve():
    assert solve('4 20 2 10') == '2'
    assert solve('1 1000000000000000000 10 1000000000') == '1000000007'
