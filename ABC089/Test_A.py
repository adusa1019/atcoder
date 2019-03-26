import pytest
from A import solve


def test_solve():
    assert solve('8') == '2'
    assert solve('2') == '0'
    assert solve('9') == '3'
