import pytest
from C import solve


def test_solve():
    assert solve('101') == '4'
    assert solve('2') == '-1'
    assert solve('999983') == '999982'
