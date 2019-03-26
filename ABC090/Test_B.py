import pytest
from B import solve


def test_solve():
    assert solve('11009 11332') == '4'
    assert solve('31415 92653') == '612'
