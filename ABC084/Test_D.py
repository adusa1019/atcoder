import pytest
from D import solve


def test_solve():
    assert solve('1\n3 7') == '2'
    assert solve('4\n13 13\n7 11\n7 11\n2017 2017') == '1\n0\n0\n1'
    assert solve('6\n1 53\n13 91\n37 55\n19 51\n73 91\n13 49') == '4\n4\n1\n1\n1\n2'
