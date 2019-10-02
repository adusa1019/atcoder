import pytest
from E import solve


def test_solve():
    assert solve('10') == '5'
    assert solve('1111111111111111111') == '162261460'
