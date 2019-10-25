import pytest
from B import solve


def test_solve():
    assert solve('3\n3 1 2') == '11'
    assert solve('7\n5 0 7 8 3 3 2') == '312'
