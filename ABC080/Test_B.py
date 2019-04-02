import pytest
from B import solve


def test_solve():
    assert solve('12') == 'Yes'
    assert solve('57') == 'No'
    assert solve('148') == 'No'
