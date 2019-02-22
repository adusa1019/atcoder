import pytest
from B import solve


def test_solve():
    assert solve('4\n3 8 5 1') == 'Yes'
    assert solve('4\n3 8 4 1') == 'No'
    assert solve('10\n1 8 10 5 8 12 34 100 11 3') == 'No'
