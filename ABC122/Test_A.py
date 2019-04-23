import pytest
from A import solve


def test_solve():
    assert solve('A') == 'T'
    assert solve('G') == 'C'
