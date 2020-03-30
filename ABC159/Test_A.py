import pytest
from A import solve


def test_solve():
    assert solve('2 1') == '1'
    assert solve('4 3') == '9'
    assert solve('1 1') == '0'
    assert solve('13 3') == '81'
    assert solve('0 3') == '3'
