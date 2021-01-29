import pytest
from A import solve


def test_solve():
    assert solve('200 300') == '200'
    assert solve('10000 0') == '20100'
