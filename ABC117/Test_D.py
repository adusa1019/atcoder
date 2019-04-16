import pytest
from D import solve


def test_solve():
    # """
    assert solve('1 7\n0') == '7'
    assert solve('1 9\n0') == '9'
    assert solve('1 7\n128') == '135'
    assert solve('1 7\n0') == '7'
    assert solve('4 7\n1 6 8 3') == '26'
    # """
    assert solve('3 7\n1 6 3') == '14'
    assert solve('4 9\n7 4 0 3') == '46'
    assert solve('1 0\n1000000000000') == '1000000000000'
