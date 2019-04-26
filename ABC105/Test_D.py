import pytest
from D import solve


def test_solve():
    assert solve('3 2\n4 1 5') == '3'
    assert solve('13 17\n29 7 5 7 9 51 7 13 8 55 42 9 81') == '6'
    assert solve(
        '10 400000000\n1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000'
    ) == '25'
    n, m, a = 10**5, 10**5, " ".join(["1"] * 10**5)
    assert solve("{} {}\n{}".format(n, m, a)) == "1"
