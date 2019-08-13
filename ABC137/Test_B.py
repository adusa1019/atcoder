import pytest
from B import solve


def test_solve():
    assert solve('3 7') == '5 6 7 8 9'
    assert solve('4 0') == '-3 -2 -1 0 1 2 3'
    assert solve('1 100') == '100'
