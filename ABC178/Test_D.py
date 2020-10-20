import pytest
from D import solve


def test_solve():
    assert solve('7') == '3'
    assert solve('2') == '0'
    assert solve('1729') == '294867501'
