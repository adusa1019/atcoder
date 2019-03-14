import pytest
from A import solve


def test_solve():
    assert solve('999') == 'ABC'
    assert solve('1000') == 'ABD'
    assert solve('1481') == 'ABD'
