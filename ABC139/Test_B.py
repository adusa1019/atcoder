import pytest
from B import solve


def test_solve():
    assert solve('4 10') == '3'
    assert solve('8 9') == '2'
    assert solve('8 8') == '1'
