import pytest
from A import solve


def test_solve():
    assert solve('ABC') == 'ARC'
