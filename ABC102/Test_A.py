import pytest
from A import solve


def test_solve():
    assert solve('3') == '6'
    assert solve('10') == '10'
    assert solve('999999999') == '1999999998'
