import pytest
from C import solve


def test_solve():
    assert solve('198 1.10') == '217'
    assert solve('1 0.01') == '0'
    assert solve('1000000000000000 9.99') == '9990000000000000'
