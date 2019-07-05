import pytest
from D import solve


def test_solve():
    assert solve('5 3') == '3\n6\n1'
    assert solve('2000 3') == '1998\n3990006\n327341989'
