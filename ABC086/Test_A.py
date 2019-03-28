import pytest
from A import solve


def test_solve():
    assert solve('3 4') == 'Even'
    assert solve('1 21') == 'Odd'
