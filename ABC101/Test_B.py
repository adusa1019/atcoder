import pytest
from B import solve


def test_solve():
    assert solve('12') == 'Yes'
    assert solve('101') == 'No'
    assert solve('999999999') == 'Yes'
