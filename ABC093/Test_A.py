import pytest
from A import solve


def test_solve():
    assert solve('bac') == 'Yes'
    assert solve('bab') == 'No'
    assert solve('abc') == 'Yes'
    assert solve('aaa') == 'No'
