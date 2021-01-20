import pytest
from B import solve


def test_solve():
    assert solve('5\n1 2\n6 6\n4 4\n3 3\n3 2') == 'Yes'
    assert solve('5\n1 1\n2 2\n3 4\n5 5\n6 6') == 'No'
    assert solve('6\n1 1\n2 2\n3 3\n4 4\n5 5\n6 6') == 'Yes'
