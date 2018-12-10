import pytest
from A import solve


def test_solve():
    assert solve('25') == 'Christmas'
    assert solve('22') == 'Christmas Eve Eve Eve'
