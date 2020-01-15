import pytest
from A import solve


def test_solve():
    assert solve('2 900') == 'Yes'
    assert solve('1 501') == 'No'
    assert solve('4 2000') == 'Yes'
