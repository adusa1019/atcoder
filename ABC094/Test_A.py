import pytest
from A import solve


def test_solve():
    assert solve('3 5 4') == 'YES'
    assert solve('2 2 6') == 'NO'
    assert solve('5 3 2') == 'NO'
