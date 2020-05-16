import pytest
from B import solve


def test_solve():
    assert solve('10 9 10 10') == 'No'
    assert solve('46 4 40 5') == 'Yes'
