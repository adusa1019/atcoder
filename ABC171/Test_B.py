import pytest
from B import solve


def test_solve():
    assert solve('5 3\n50 100 80 120 80') == '210'
    assert solve('1 1\n1000') == '1000'
