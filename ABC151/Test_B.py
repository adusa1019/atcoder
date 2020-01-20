import pytest
from B import solve


def test_solve():
    assert solve('5 10 7\n8 10 3 6') == '8'
    assert solve('4 100 60\n100 100 100') == '0'
    assert solve('4 100 60\n0 0 0') == '-1'
