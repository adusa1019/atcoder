import pytest
from B import solve


def test_solve():
    assert solve('3 6\n3 4 5') == '2'
    assert solve('4 9\n3 3 3 3') == '4'
