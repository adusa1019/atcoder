import pytest
from C import solve


def test_solve():
    assert solve('2 3 1 2') == '3.0 0'
    assert solve('2 2 1 1') == '2.0 1'
