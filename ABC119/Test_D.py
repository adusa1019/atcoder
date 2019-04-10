import pytest
from D import solve


def test_solve():
    assert solve('2 3 4\n100\n600\n400\n900\n1000\n150\n2000\n899\n799') == '350\n1400\n301\n399'
    assert solve('1 1 3\n1\n10000000000\n2\n9999999999\n5000000000') == '10000000000\n10000000000\n14999999998'
    assert solve('1 2 1\n5\n0\n2\n1') == '4'
