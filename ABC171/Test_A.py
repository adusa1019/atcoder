import pytest
from A import solve


def test_solve():
    assert solve('B') == 'A'
    assert solve('a') == 'a'
