import pytest
from B import solve


def test_solve():
    assert solve('1024') == '2020'
    assert solve('0') == '0'
    assert solve('1000000000') == '2000000000'
