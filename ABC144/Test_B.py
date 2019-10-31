import pytest
from B import solve


def test_solve():
    assert solve('10') == 'Yes'
    assert solve('50') == 'No'
    assert solve('81') == 'Yes'
