import pytest
from B import solve


def test_solve():
    assert solve('3 8 2') == '3\n4\n7\n8'
    assert solve('4 8 3') == '4\n5\n6\n7\n8'
    assert solve('2 9 100') == '2\n3\n4\n5\n6\n7\n8\n9'
