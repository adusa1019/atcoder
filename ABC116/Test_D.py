import pytest
from D import solve


def test_solve():
    assert solve('6 3\n1 9\n1 7\n1 6\n2 5\n3 5\n2 1') == '28'
    assert solve('5 3\n1 9\n1 7\n2 6\n2 5\n3 1') == '26'
    assert solve('7 4\n1 1\n2 1\n3 1\n4 6\n4 5\n4 5\n4 5') == '25'
    assert solve(
        '6 5\n5 1000000000\n2 990000000\n3 980000000\n6 970000000\n6 960000000\n4 950000000'
    ) == '4900000016'
