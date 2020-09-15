import pytest
from A import solve


def test_solve():
    assert solve('2') == '14'
    assert solve('10') == '1110'
