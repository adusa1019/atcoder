import pytest
from C import solve


def test_solve():
    assert solve('4\n2 4 4 3') == '4\n3\n3\n4'
    assert solve('2\n1 2') == '2\n1'
    assert solve('6\n5 5 4 4 3 3') == '4\n4\n4\n4\n4\n4'
