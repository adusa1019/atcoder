import pytest
from B import solve


def test_solve():
    assert solve('29\n20\n7\n35\n120') == '215'
    assert solve('101\n86\n119\n108\n57') == '481'
    assert solve('123\n123\n123\n123\n123') == '643'
