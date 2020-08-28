import pytest
from A import solve


def test_solve():
    assert solve('RRS') == '2'
    assert solve('SSS') == '0'
    assert solve('RSR') == '1'
