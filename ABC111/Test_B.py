import pytest
from B import solve


def test_solve():
    assert solve('111') == '111'
    assert solve('112') == '222'
    assert solve('750') == '777'
