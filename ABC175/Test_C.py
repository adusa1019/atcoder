import pytest
from C import solve


def test_solve():
    assert solve('6 2 4') == '2'
    assert solve('7 4 3') == '1'
    assert solve('10 1 2') == '8'
    assert solve('1000000000000000 1000000000000000 1000000000000000') == '1000000000000000'
