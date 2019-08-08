import pytest
from C import solve


def test_solve():
    assert solve('2\n3 5 2\n4 5') == '9'
    assert solve('3\n5 6 3 8\n5 100 8') == '22'
    assert solve('2\n100 1 1\n1 100') == '3'
