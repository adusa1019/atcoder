import pytest
from A import solve


def test_solve():
    assert solve('1000 15 80') == 'Yes'
    assert solve('2000 20 100') == 'Yes'
    assert solve('10000 1 1') == 'No'
