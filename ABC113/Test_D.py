import pytest
from D import solve


def test_solve():
    assert solve('1 3 2') == '1'
    assert solve('1 3 1') == '2'
    assert solve('2 3 3') == '1'
    assert solve('2 3 1') == '5'
    assert solve('7 1 1') == '1'
    assert solve('15 8 5') == '437760187'
