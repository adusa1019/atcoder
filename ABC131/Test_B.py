import pytest
from B import solve


def test_solve():
    assert solve('5 2') == '18'
    assert solve('3 -1') == '0'
    assert solve('30 -50') == '-1044'
