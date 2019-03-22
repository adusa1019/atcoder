import pytest
from A import solve


def test_solve():
    assert solve('oxo') == '900'
    assert solve('ooo') == '1000'
    assert solve('xxx') == '700'
