import pytest
from B import solve


def test_solve():
    assert solve('11') == '9'
    assert solve('136') == '46'
    assert solve('100000') == '90909'
