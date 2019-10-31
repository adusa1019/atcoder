import pytest
from C import solve


def test_solve():
    assert solve('10') == '5'
    assert solve('50') == '13'
    assert solve('10000000019') == '10000000018'
