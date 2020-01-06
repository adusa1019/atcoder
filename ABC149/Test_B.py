import pytest
from B import solve


def test_solve():
    assert solve('2 3 3') == '0 2'
    assert solve('2 3 1') == '1 3'
    assert solve('500000000000 500000000000 1000000000000') == '0 0'
