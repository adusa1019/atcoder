import pytest
from C import solve


def test_solve():
    assert solve('4 9 2 3') == '2'
    assert solve('10 40 6 8') == '23'
    assert solve('314159265358979323 846264338327950288 419716939 937510582') == '532105071133627368'
