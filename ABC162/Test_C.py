import pytest
from C import solve


def test_solve():
    assert solve('2') == '9'
    assert solve('200') == '10813692'
