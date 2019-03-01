import pytest
from C import solve


def test_solve():
    assert solve('4\n3 1 3 2') == '1'
    assert solve('6\n105 119 105 119 105 119') == '0'
    assert solve('4\n1 1 1 1') == '2'
