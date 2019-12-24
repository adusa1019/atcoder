import pytest
from A import solve


def test_solve():
    assert solve('3\n1') == '2'
    assert solve('1\n2') == '3'
