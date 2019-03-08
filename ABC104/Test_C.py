import pytest
from C import solve


def test_solve():
    assert solve('2 700\n3 500\n5 800') == '3'
    assert solve('2 2000\n3 500\n5 800') == '7'
    assert solve('2 400\n3 500\n5 800') == '2'
    assert solve('5 25000\n20 1000\n40 1000\n50 1000\n30 1000\n1 1000') == '66'
    assert solve('3 2000\n3 500\n5 1000\n4 500') == '5'
    assert solve('3 2200\n3 500\n5 1000\n4 500') == '6'
