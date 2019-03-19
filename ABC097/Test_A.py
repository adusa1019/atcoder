import pytest
from A import solve


def test_solve():
    assert solve('4 7 9 3') == 'Yes'
    assert solve('100 10 1 2') == 'No'
    assert solve('10 10 10 1') == 'Yes'
    assert solve('1 100 2 10') == 'Yes'
