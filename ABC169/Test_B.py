import pytest
from B import solve


def test_solve():
    assert solve('2\n1000000000 1000000000') == '1000000000000000000'
    assert solve('3\n101 9901 999999000001') == '-1'
    assert solve('31\n4 1 5 9 2 6 5 3 5 8 9 7 9 3 2 3 8 4 6 2 6 4 3 3 8 3 2 7 9 5 0') == '0'
