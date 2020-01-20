import pytest
from A import solve


def test_solve():
    assert solve('3 3') == 'Yes'
    assert solve('3 2') == 'No'
    assert solve('1 1') == 'Yes'
