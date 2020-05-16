import pytest
from B import solve


def test_solve():
    assert solve('3 2\n2\n1 3\n1\n3') == '1'
    assert solve('3 3\n1\n3\n1\n3\n1\n3') == '2'
