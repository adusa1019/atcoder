import pytest
from A import solve


def test_solve():
    assert solve('1118') == 'Yes'
    assert solve('7777') == 'Yes'
    assert solve('1234') == 'No'
