import pytest
from C import solve


def test_solve():
    assert solve('5 100 90 80\n98\n40\n30\n21\n80') == '23'
    assert solve('8 100 90 80\n100\n100\n90\n90\n90\n80\n80\n80') == '0'
    assert solve('8 1000 800 100\n300\n333\n400\n444\n500\n555\n600\n666') == '243'
