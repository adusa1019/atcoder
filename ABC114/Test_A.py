import pytest
from A import solve


def test_solve():
    assert solve('5') == 'YES'
    assert solve('6') == 'NO'
