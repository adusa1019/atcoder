import pytest
from A import solve


def test_solve():
    assert solve('1234\n150\n100') == '84'
    assert solve('1000\n108\n108') == '28'
    assert solve('579\n123\n456') == '0'
    assert solve('7477\n549\n593') == '405'
