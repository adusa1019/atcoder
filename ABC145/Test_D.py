import pytest
from D import solve


def test_solve():
    assert solve('3 3') == '2'
    assert solve('2 2') == '0'
    assert solve('999999 999999') == '151840682'
