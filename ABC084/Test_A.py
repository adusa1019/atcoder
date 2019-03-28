import pytest
from A import solve


def test_solve():
    assert solve('21') == '27'
    assert solve('12') == '36'
