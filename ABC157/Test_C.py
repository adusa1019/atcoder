import pytest
from C import solve


def test_solve():
    assert solve('3 3\n1 7\n3 2\n1 7') == '702'
    assert solve('3 2\n2 1\n2 3') == '-1'
    assert solve('3 1\n1 0') == '-1'
    assert solve('1 0') == '0'
    assert solve('1 1\n1 0') == '0'
