import pytest
from C import solve


def test_solve():
    assert solve('8 3\nACACTACG\n3 7\n2 3\n1 8') == '2\n0\n3'
