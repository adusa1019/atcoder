import pytest
from A import solve


def test_solve():
    assert solve('2') == '8'
    assert solve('1') == '1'
