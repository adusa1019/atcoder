import pytest
from B import solve


def test_solve():
    assert solve('1 1 7 2') == '3.0'
    assert solve('1 1 3 2') == '1.6666666667'
    assert solve('-9 99 -999 9999') == '-18.7058823529'
