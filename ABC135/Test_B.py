import pytest
from B import solve


def test_solve():
    assert solve('5\n5 2 3 4 1') == 'YES'
    assert solve('5\n2 4 3 5 1') == 'NO'
    assert solve('7\n1 2 3 4 5 6 7') == 'YES'
