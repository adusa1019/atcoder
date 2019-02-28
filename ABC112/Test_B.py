import pytest
from B import solve


def test_solve():
    assert solve('3 70\n7 60\n1 80\n4 50') == '4'
    assert solve('4 3\n1 1000\n2 4\n3 1000\n4 500') == 'TLE'
    assert solve('5 9\n25 8\n5 9\n4 10\n1000 1000\n6 1') == '5'
