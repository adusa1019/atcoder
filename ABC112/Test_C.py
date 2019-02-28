import pytest
from C import solve


def test_solve():
    assert solve('4\n2 3 5\n2 1 5\n1 2 5\n3 2 5') == '2 2 6'
    assert solve('2\n0 0 100\n1 1 98') == '0 0 100'
    assert solve('3\n99 1 191\n100 1 192\n99 0 192') == '100 0 193'
