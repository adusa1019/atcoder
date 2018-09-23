import pytest
from B import solve


def test_solve():
    assert solve('0 0 0 1') == '-1 1 -1 0'
    assert solve('2 3 6 6') == '3 10 -1 7'
    assert solve('31 -41 -59 26') == '-126 -64 -36 -131'
