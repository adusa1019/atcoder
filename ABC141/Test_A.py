import pytest
from A import solve


def test_solve():
    assert solve('Sunny') == 'Cloudy'
    assert solve('Rainy') == 'Sunny'
