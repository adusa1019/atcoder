import pytest
from C import solve


def test_solve():
    assert solve('2 3') == '6'
    assert solve('123 456') == '18696'
    assert solve('100000 99999') == '9999900000'
