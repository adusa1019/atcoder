import pytest
from B import solve


def test_solve():
    assert solve('2 3 -10\n1 2 3\n3 2 1\n1 2 2') == '1'
    assert solve('5 2 -4\n-2 5\n100 41\n100 40\n-3 0\n-6 -2\n18 -13') == '2'
    assert solve('3 3 0\n100 -100 0\n0 100 100\n100 100 100\n-100 100 100') == '0'
