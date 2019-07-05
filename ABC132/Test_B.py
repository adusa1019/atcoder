import pytest
from B import solve


def test_solve():
    assert solve('5\n1 3 5 4 2') == '2'
    assert solve('9\n9 6 3 2 5 8 7 4 1') == '5'
