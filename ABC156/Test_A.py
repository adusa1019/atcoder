import pytest
from A import solve


def test_solve():
    assert solve('2 2919') == '3719'
    assert solve('22 3051') == '3051'
