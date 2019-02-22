import pytest
from B import solve


def test_solve():
    assert solve('8') == '5'
    assert solve('7') == '18'
    assert solve('54') == '114'
