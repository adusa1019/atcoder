import pytest
from A import solve


def test_solve():
    assert abs(solve('8 3') - 2.6666666667) < 10**(-3)
    assert abs(solve('99 1') - 99.0000000000) < 10**(-3)
    assert abs(solve('1 100') - 0.0100000000) < 10**(-3)
