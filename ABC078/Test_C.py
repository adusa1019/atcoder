import pytest
from C import solve


def test_solve():
    assert solve('1 1') == '3800'
    assert solve('10 2') == '18400'
    assert solve('100 5') == '608000'
