import pytest
from D import solve


def test_solve():
    assert solve('33') == '2 -1'
    assert solve('1') == '0 -1'
