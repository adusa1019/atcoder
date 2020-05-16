import pytest
from D import solve


def test_solve():
    assert solve('5 7 4') == '2'
    assert solve('11 10 9') == '9'
