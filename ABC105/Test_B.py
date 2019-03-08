import pytest
from B import solve


def test_solve():
    assert solve('11') == 'Yes'
    assert solve('40') == 'Yes'
    assert solve('3') == 'No'
