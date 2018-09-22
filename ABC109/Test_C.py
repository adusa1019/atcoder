import pytest
from C import solve


def test_solve():
    assert solve('3 3\n1 7 11') == '2'
    assert solve('3 81\n33 105 57') == '24'
    assert solve('1 1\n1000000000') == '999999999'
