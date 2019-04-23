import pytest
from B import solve


def test_solve():
    assert solve('ATCODER') == '3'
    assert solve('HATAGAYA') == '5'
    assert solve('SHINJUKU') == '0'
