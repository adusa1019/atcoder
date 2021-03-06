import pytest
from C import solve


def test_solve():
    assert solve('4\n0 1\n0 2\n0 3\n1 1') == 'Yes'
    assert solve('14\n5 5\n0 1\n2 5\n8 0\n2 1\n0 0\n3 6\n8 6\n5 9\n7 9\n3 4\n9 2\n9 8\n7 2') == 'No'
    assert solve('9\n8 2\n2 3\n1 3\n3 7\n1 0\n8 8\n5 6\n9 7\n0 1') == 'Yes'
