import pytest
from A import solve


def test_solve():
    assert solve('2 2') == '1'
    assert solve('5 7') == '24'
