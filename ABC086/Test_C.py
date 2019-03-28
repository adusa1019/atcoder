import pytest
from C import solve


def test_solve():
    assert solve('2\n3 1 2\n6 1 1') == 'Yes'
    assert solve('1\n2 100 100') == 'No'
    assert solve('2\n5 1 1\n100 1 1') == 'No'
