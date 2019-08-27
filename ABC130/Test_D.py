import pytest
from D import solve


def test_solve():
    assert solve('4 10\n6 1 2 7') == '2'
    assert solve('3 5\n3 3 3') == '3'
    assert solve('10 53462\n103 35322 232 342 21099 90000 18843 9010 35221 19352') == '36'
