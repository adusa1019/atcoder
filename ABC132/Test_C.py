import pytest
from C import solve


def test_solve():
    assert solve('6\n9 1 4 4 6 7') == '2'
    assert solve('8\n9 1 14 5 5 4 4 14') == '0'
    assert solve('14\n99592 10342 29105 78532 83018 11639 92015 77204 30914 21912 34519 80835 100000 1') == '42685'
