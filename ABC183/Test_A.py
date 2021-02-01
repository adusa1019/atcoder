import pytest
from A import solve


def test_solve():
    assert solve('1') == '1'
    assert solve('0') == '0'
    assert solve('-1') == '0'
