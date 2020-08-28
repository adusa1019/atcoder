import pytest
from B import solve


def test_solve():
    assert solve('5\n4 4 9 7 5') == '5'
    assert solve('6\n4 5 4 3 3 5') == '8'
    assert solve('10\n9 4 6 1 9 6 10 6 6 8') == '39'
    assert solve('2\n1 1') == '0'
