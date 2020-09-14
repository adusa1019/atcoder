import pytest
from D import solve


def test_solve():
    assert solve('4\nWWRR') == '2'
    assert solve('2\nRR') == '0'
    assert solve('8\nWRWWRWRR') == '3'
