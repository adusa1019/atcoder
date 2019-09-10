import pytest
from C import solve


def test_solve():
    assert solve('3\n2 5') == '9'
    assert solve('2\n3') == '6'
    assert solve('6\n0 153 10 10 23') == '53'
