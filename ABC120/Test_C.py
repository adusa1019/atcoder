import pytest
from C import solve


def test_solve():
    assert solve('0011') == '4'
    assert solve('11011010001011') == '12'
    assert solve('0') == '0'
