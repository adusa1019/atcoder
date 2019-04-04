import pytest
from B import solve


def test_solve():
    assert solve('4\n3') == '10'
    assert solve('10\n10') == '76'
