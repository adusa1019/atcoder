import pytest
from A import solve


def test_solve():
    assert solve('1') == '6.28318530717958623200'
    assert solve('73') == '458.67252742410977361942'
