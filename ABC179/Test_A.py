import pytest
from A import solve


def test_solve():
    assert solve('apple') == 'apples'
    assert solve('bus') == 'buses'
    assert solve('box') == 'boxs'
