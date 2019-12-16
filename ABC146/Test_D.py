import pytest
from D import solve


def test_solve():
    assert solve('3\n1 2\n2 3') == '2\n1\n2'
    assert solve('8\n1 2\n2 3\n2 4\n2 5\n4 7\n5 6\n6 8') == '4\n1\n2\n3\n4\n1\n1\n2'
    assert solve('6\n1 2\n1 3\n1 4\n1 5\n1 6') == '5\n1\n2\n3\n4\n5'
