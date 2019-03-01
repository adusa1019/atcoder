import pytest
from A import solve


def test_solve():
    assert solve('119') == '991'
    assert solve('999') == '111'
