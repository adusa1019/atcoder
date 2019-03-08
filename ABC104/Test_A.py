import pytest
from A import solve


def test_solve():
    assert solve('1199') == 'ABC'
    assert solve('1200') == 'ARC'
    assert solve('4208') == 'AGC'
