import pytest
from C import solve


def test_solve():
    # assert solve('3\n0 0\n1 0\n0 1') == '2.2761423749'
    # assert solve('2\n-879 981\n-866 890') == '91.9238815543'
    assert solve('8\n-406 10\n512 859\n494 362\n-955 -475\n128 553\n-986 -885\n763 77\n449 310') == '7641.9817824387'
