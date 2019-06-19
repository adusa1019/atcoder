import pytest
from A import solve


def test_solve():
    assert solve('1 3') == '3'
    assert solve('0 1') == '0'
    assert solve('32 21') == '58'
