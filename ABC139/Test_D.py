import pytest
from D import solve


def test_solve():
    assert solve('2') == '1'
    assert solve('13') == '78'
    assert solve('1') == '0'
