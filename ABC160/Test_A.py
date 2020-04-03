import pytest
from A import solve


def test_solve():
    assert solve('sippuu') == 'Yes'
    assert solve('iphone') == 'No'
    assert solve('coffee') == 'Yes'
