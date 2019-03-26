import pytest
from B import solve


def test_solve():
    assert solve('2\n3 1') == '2'
    assert solve('3\n2 7 4') == '5'
    assert solve('4\n20 18 2 18') == '18'
