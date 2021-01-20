import pytest
from C import solve


def test_solve():
    assert solve('3') == '3'
    assert solve('100') == '473'
    assert solve('1000000') == '13969985'
