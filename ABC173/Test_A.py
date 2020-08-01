import pytest
from A import solve


def test_solve():
    assert solve('1900') == '100'
    assert solve('3000') == '0'
