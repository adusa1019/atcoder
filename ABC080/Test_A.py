import pytest
from A import solve


def test_solve():
    assert solve('7 17 120') == '119'
    assert solve('5 20 100') == '100'
    assert solve('6 18 100') == '100'
