import pytest
from C import solve


def test_solve():
    assert solve('9 45000') == '4 0 5'
    assert solve('20 196000') == '-1 -1 -1'
    assert solve('1000 1234000') == '14 27 959'
    assert solve('2000 20000000') == '2000 0 0'
