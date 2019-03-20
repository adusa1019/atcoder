import pytest
from B import solve


def test_solve():
    assert solve('5 3 11\n1') == '30'
    assert solve('3 3 4\n2') == '22'
