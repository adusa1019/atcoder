import pytest
from B import solve


def test_solve():
    assert solve('2\n2\n2\n100') == '2'
    assert solve('5\n1\n0\n150') == '0'
    assert solve('30\n40\n50\n6000') == '213'
