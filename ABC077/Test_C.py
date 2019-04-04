import pytest
from C import solve


def test_solve():
    assert solve('2\n1 5\n2 4\n3 6') == '3'
    assert solve('3\n1 1 1\n2 2 2\n3 3 3') == '27'
    assert solve('6\n3 14 159 2 6 53\n58 9 79 323 84 6\n2643 383 2 79 50 288') == '87'
