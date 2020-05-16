import pytest
from A import solve


def test_solve():
    assert solve('4 5') == 'unsafe'
    assert solve('100 2') == 'safe'
    assert solve('10 10') == 'unsafe'
