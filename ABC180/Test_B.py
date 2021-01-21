import pytest
from B import solve


def test_solve():
    assert solve('2\n2 -1') == '3\n2.23606797749979\n2'
    assert solve('10\n3 -1 -4 1 -5 9 2 -6 5 -3') == '39\n14.38749456993816\n9'
