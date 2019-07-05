import pytest
from A import solve


def test_solve():
    assert solve('ASSA') == 'Yes'
    assert solve('STOP') == 'No'
    assert solve('FFEE') == 'Yes'
    assert solve('FREE') == 'No'
