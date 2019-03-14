import pytest
from C import solve


def test_solve():
    assert solve('127') == '4'
    assert solve('3') == '3'
    assert solve('44852') == '16'
    assert solve('100000') == '16'
