import pytest
from A import solve


def test_solve():
    assert solve('3 1') == 'Yes'
    assert solve('1 2') == 'No'
    assert solve('2 2') == 'No'
