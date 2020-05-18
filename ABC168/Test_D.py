import pytest
from D import solve


def test_solve():
    assert solve('4 4\n1 2\n2 3\n3 4\n4 2') == 'Yes\n1\n2\n2'
    assert solve('6 9\n3 4\n6 1\n2 4\n5 3\n4 6\n1 5\n6 2\n4 5\n5 6') == 'Yes\n6\n5\n6\n1\n1'
