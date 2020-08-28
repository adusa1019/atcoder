import pytest
from A import solve


def test_solve():
    assert solve('25') == 'No'
    assert solve('30') == 'Yes'
