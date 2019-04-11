import pytest
from D import solve


def test_solve():
    assert solve('20 4\n3 7 8 4') == '777773'
    assert solve(
        '101 9\n9 8 7 6 5 4 3 2 1') == '71111111111111111111111111111111111111111111111111'
    assert solve('15 3\n5 4 6') == '654'
    assert solve('15 3\n2 3 5') == '555'
    assert solve('11 3\n6 1 5 8') == '5111'
