import pytest
from A import solve


def test_solve():
    assert solve('1 2 3') == '3 1 2'
    assert solve('100 100 100') == '100 100 100'
    assert solve('41 59 31') == '31 41 59'
