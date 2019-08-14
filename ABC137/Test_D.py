import pytest
from D import solve


def test_solve():
    assert solve('3 4\n4 3\n4 1\n2 2') == '5'
    assert solve('5 3\n1 2\n1 3\n1 4\n2 1\n2 3') == '10'
    assert solve('1 1\n2 1') == '0'
    assert solve('3 3\n3 5\n2 1\n1 2') == '8'
    assert solve('5 3\n3 5\n2 1\n1 2\n3 8\n2 4') == '14'
    assert solve('5 3\n3 5\n2 9\n1 2\n3 8\n2 9') == '20'
