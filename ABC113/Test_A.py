import pytest
from A import solve


def test_solve():
    assert solve('81 58') == '110'
    assert solve('4 54') == '31'
