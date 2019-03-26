import pytest
from C import solve


def test_solve():
    assert solve('1 0 1\n2 1 2\n1 0 1') == 'Yes'
    assert solve('2 2 2\n2 1 2\n2 2 2') == 'No'
    assert solve('0 8 8\n0 8 8\n0 8 8') == 'Yes'
    assert solve('1 8 6\n2 9 7\n0 7 7') == 'No'
