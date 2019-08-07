import pytest
from D import solve


def test_solve():
    assert solve('5 1\n00010') == '4'
    assert solve('14 2\n11101010110011') == '8'
    assert solve('1 1\n1') == '1'
