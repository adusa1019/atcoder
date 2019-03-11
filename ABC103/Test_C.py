import pytest
from C import solve


def test_solve():
    assert solve('3\n3 4 6') == '10'
    assert solve('5\n7 46 11 20 11') == '90'
    assert solve('7\n994 518 941 851 647 2 581') == '4527'
