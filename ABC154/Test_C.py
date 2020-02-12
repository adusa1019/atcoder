import pytest
from C import solve


def test_solve():
    assert solve('5\n2 6 1 4 5') == 'YES'
    assert solve('6\n4 1 3 1 6 2') == 'NO'
    assert solve('2\n10000000 10000000') == 'NO'
