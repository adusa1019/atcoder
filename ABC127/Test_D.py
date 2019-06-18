import pytest
from D import solve


def test_solve():
    assert solve('3 2\n5 1 4\n2 3\n1 5') == '14'
    assert solve('10 3\n1 8 5 7 100 4 52 33 13 5\n3 10\n4 30\n1 4') == '338'
    assert solve('3 2\n100 100 100\n3 99\n3 99') == '300'
    assert solve('11 3\n1 1 1 1 1 1 1 1 1 1 1\n3 1000000000\n4 1000000000\n3 1000000000') == '10000000001'
    assert solve('3 2\n100 100 100\n5 1000\n3 99') == '3000'
