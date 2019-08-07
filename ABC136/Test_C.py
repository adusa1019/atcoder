import pytest
from C import solve


def test_solve():
    assert solve('5\n1 2 1 1 3') == 'Yes'
    assert solve('4\n1 3 2 1') == 'No'
    assert solve('5\n1 2 3 4 5') == 'Yes'
    assert solve('1\n1000000000') == 'Yes'
