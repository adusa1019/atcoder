import pytest
from A import solve


def test_solve():
    assert solve('16') == 'pon'
    assert solve('2') == 'hon'
    assert solve('183') == 'bon'
