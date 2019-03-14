import pytest
from A import solve


def test_solve():
    assert solve('5 4') == 'Yay!'
    assert solve('8 8') == 'Yay!'
    assert solve('11 4') == ':('
