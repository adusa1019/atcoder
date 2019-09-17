import pytest
from C import solve


def test_solve():
    assert solve('6 3 4\n3\n1\n3\n2') == 'No\nNo\nYes\nNo\nNo\nNo'
    assert solve('6 5 4\n3\n1\n3\n2') == 'Yes\nYes\nYes\nYes\nYes\nYes'
    assert solve('10 13 15\n3\n1\n4\n1\n5\n9\n2\n6\n5\n3\n5\n8\n9\n7\n9') == 'No\nNo\nNo\nNo\nYes\nNo\nNo\nNo\nYes\nNo'
