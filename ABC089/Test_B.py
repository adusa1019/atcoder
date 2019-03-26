import pytest
from B import solve


def test_solve():
    assert solve('6\nG W Y P Y W') == 'Four'
    assert solve('9\nG W W G P W P G G') == 'Three'
    assert solve('8\nP Y W G Y W Y Y') == 'Four'
