import pytest
from A import solve


def test_solve():
    assert solve('100 1 2') == '101'
    assert solve('100 2 1') == '99'
    assert solve('100 1 1') == '100'
