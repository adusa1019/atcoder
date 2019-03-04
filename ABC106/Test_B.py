import pytest
from B import solve


def test_solve():
    assert solve('105') == '1'
    assert solve('7') == '0'
    assert solve('198') == '2'
    assert solve('197') == '1'
