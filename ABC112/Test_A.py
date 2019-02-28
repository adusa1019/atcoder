import pytest
from A import solve


def test_solve():
    assert solve('1') == 'Hello World'
    assert solve('2\n3\n5') == '8'
