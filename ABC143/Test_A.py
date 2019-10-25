import pytest
from A import solve


def test_solve():
    assert solve('12 4') == '4'
    assert solve('20 15') == '0'
    assert solve('20 30') == '0'
