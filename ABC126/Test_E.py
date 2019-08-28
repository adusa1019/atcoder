import pytest
from E import solve


def test_solve():
    assert solve('3 1\n1 2 1') == '2'
    assert solve('6 5\n1 2 1\n2 3 2\n1 3 3\n4 5 4\n5 6 5') == '2'
    assert solve('6 5\n1 3 1\n2 3 2\n1 5 3\n4 5 4\n5 6 5') == '1'
    assert solve('100000 1\n1 100000 100') == '99999'
