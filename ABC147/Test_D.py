import pytest
from D import solve


def test_solve():
    assert solve('3\n1 2 3') == '6'
    assert solve('10\n3 1 4 1 5 9 2 6 5 3') == '237'
    assert solve(
        '10\n3 14 159 2653 58979 323846 2643383 27950288 419716939 9375105820') == '103715602'
    assert solve('100000\n' + "\n".join(['1'*12 for i in range(10**5)])) == "0"
