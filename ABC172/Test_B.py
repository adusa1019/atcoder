import pytest
from B import solve


def test_solve():
    assert solve('cupofcoffee\ncupofhottea') == '4'
    assert solve('abcde\nbcdea') == '5'
    assert solve('apple\napple') == '0'
