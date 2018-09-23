import pytest
from A import solve


def test_solve():
    assert solve('3') == '2'
    assert solve('6') == '9'
    assert solve('11') == '30'
    assert solve('50') == '625'
