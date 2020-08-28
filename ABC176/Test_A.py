import pytest
from A import solve


def test_solve():
    assert solve('20 12 6') == '12'
    assert solve('1000 1 1000') == '1000000'
