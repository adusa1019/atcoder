import pytest
from A import solve


def test_solve():
    assert solve('a') == 'b'
    assert solve('y') == 'z'
