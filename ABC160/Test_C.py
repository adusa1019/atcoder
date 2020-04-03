import pytest
from C import solve


def test_solve():
    assert solve('20 3\n5 10 15') == '10'
    assert solve('20 3\n0 5 15') == '10'
