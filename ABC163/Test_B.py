import pytest
from B import solve


def test_solve():
    assert solve('41 2\n5 6') == '30'
    assert solve('10 2\n5 6') == '-1'
    assert solve('11 2\n5 6') == '0'
    assert solve('314 15\n9 26 5 35 8 9 79 3 23 8 46 2 6 43 3') == '9'
