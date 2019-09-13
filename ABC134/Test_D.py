import pytest
from D import solve


def test_solve():
    assert solve('3\n1 0 0') == '1\n1'
    assert solve('5\n0 0 0 0 0') == '0'
    assert solve('10\n0 0 1 0 1 1 0 1 0 1') == '4\n4 6 8 10'
    assert solve('200000\n' + ' '.join(['1'] * 200000)) == ""
