import pytest
from C import solve


def test_solve():
    assert solve('2 5 4') == '2'
    assert solve('2 6 3') == '5'
    assert solve('31 41 5') == '23'
