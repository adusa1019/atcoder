import pytest
from A import solve


def test_solve():
    assert solve('2') == '4'
    assert solve('100') == '10000'
