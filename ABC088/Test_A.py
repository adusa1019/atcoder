import pytest
from A import solve


def test_solve():
    assert solve('2018\n218') == 'Yes'
    assert solve('2763\n0') == 'No'
    assert solve('37\n514') == 'Yes'
