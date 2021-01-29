import pytest
from B import solve


def test_solve():
    assert solve('3\n3 12 7') == '3'
    assert solve('5\n8 9 18 90 72') == '2'
    assert solve('5\n1000 1000 1000 1000 1000') == '2'
