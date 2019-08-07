import pytest
from B import solve


def test_solve():
    assert solve('4\n6 5 6 8') == '3'
    assert solve('5\n4 5 3 5 4') == '3'
    assert solve('5\n9 5 6 8 4') == '1'
