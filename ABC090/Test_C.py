import pytest
from C import solve


def test_solve():
    assert solve('2 2') == '0'
    assert solve('1 7') == '5'
    assert solve('314 1592') == '496080'
