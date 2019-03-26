import pytest
from D import solve


def test_solve():
    assert solve('3 3 2\n1 4 3\n2 5 7\n8 9 6\n1\n4 8') == '5'
    assert solve('4 2 3\n3 7\n1 4\n5 2\n6 8\n2\n2 2\n2 2') == '0\n0'
    assert solve('5 5 4\n13 25 7 15 17\n16 22 20 2 9\n14 11 12 1 19\n10 6 23 8 18\n3 21 5 24 4\n3\n13 13\n2 10\n13 13') == '0\n5\n0'
