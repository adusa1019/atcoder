import pytest
from C import solve


def test_solve():
    assert solve('3\n1 3 2\n3 1 2') == '3'
    assert solve('8\n7 3 5 4 2 1 6 8\n3 8 2 5 4 6 7 1') == '17517'
    assert solve('3\n1 2 3\n1 2 3') == '0'
