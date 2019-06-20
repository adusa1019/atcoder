import pytest
from B import solve


def test_solve():
    assert solve('3\n1 2 3') == '0'
    assert solve('4\n1 3 1 1') == '2'
    assert solve('8\n27 23 76 2 3 5 62 52') == '2'
