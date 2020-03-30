import pytest
from C import solve


def test_solve():
    assert solve('3') == '1.0'
    assert solve('999') == '36926037.0'
