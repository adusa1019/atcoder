import pytest
from A import solve


def test_solve():
    assert solve('2 5') == '10'
    assert solve('5 10') == '-1'
    assert solve('9 9') == '81'
