import pytest
from D import solve


def test_solve():
    assert solve('4\n3 4 2 1') == '1'
    assert solve('3\n1 1000 1') == '0'
    assert solve('7\n218 786 704 233 645 728 389') == '23'
