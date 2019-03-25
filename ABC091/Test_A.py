import pytest
from A import solve


def test_solve():
    assert solve('50 100 120') == 'Yes'
    assert solve('500 100 1000') == 'No'
    assert solve('19 123 143') == 'No'
    assert solve('19 123 142') == 'Yes'
