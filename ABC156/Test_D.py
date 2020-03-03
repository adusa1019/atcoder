import pytest
from D import solve


def test_solve():
    assert solve('4 1 3') == '7'
    assert solve('1000000000 141421 173205') == '34076506'
