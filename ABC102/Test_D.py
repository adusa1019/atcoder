import pytest
from D import solve


def test_solve():
    import random
    n = 2 * 10**5
    # assert (solve("%d\n%s" %
                #   (n, " ".join([str(random.randint(1, 10**9)) for _ in range(n)])))) == ""
    assert solve('5\n3 2 4 1 2') == '2'
    assert solve('10\n10 71 84 33 6 47 23 25 52 64') == '36'
    assert solve('7\n1 2 3 1000000000 4 5 6') == '999999994'
