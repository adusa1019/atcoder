import pytest
from A import solve


def test_solve():
    assert solve('3200\npink') == 'pink'
    assert solve('3199\npink') == 'red'
    assert solve('4049\nred') == 'red'
