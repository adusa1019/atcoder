import pytest
from A import solve


def test_solve():
    assert solve('2 5') == '10'
    assert solve('100 100') == '10000'
