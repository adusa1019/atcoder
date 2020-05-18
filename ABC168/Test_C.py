import pytest
from C import solve


def test_solve():
    assert solve('3 4 9 0') == '5.0'
    assert solve('3 4 10 40') == '4.56425719433005567605'
