import pytest
from B import solve


def test_solve():
    assert solve('8 13') == '2'
    assert solve('54 65') == '1'
