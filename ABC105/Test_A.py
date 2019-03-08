import pytest
from A import solve


def test_solve():
    assert solve('7 3') == '1'
    assert solve('100 10') == '0'
    assert solve('1 1') == '0'
