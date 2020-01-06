import pytest
from C import solve


def test_solve():
    assert solve('20') == '23'
    assert solve('2') == '2'
    assert solve('99992') == '100003'
