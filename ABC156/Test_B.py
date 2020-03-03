import pytest
from B import solve


def test_solve():
    assert solve('11 2') == '4'
    assert solve('1010101 10') == '7'
    assert solve('314159265 3') == '18'
