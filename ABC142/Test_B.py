import pytest
from B import solve


def test_solve():
    assert solve('4 150\n150 140 100 200') == '2'
    assert solve('1 500\n499') == '0'
    assert solve('5 1\n100 200 300 400 500') == '5'
