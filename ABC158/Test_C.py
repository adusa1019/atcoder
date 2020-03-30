import pytest
from C import solve


def test_solve():
    assert solve('1 1') == '13'
    assert solve('2 2') == '25'
    assert solve('8 10') == '100'
    assert solve('19 99') == '-1'
