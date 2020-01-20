import pytest
from B import solve


def test_solve():
    assert solve('4 3') == '3333'
    assert solve('7 7') == '7777777'
