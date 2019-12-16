import pytest
from C import solve


def test_solve():
    assert solve('10 7 100') == '9'
    assert solve('2 1 100000000000') == '1000000000'
    assert solve('1000000000 1000000000 100') == '0'
    assert solve('1234 56789 314159265') == '254309'
