import pytest
from B import solve


def test_solve():
    assert solve('3 2 10 20\n8 15 13\n16 22') == 'No War'
    assert solve('4 2 -48 -1\n-20 -35 -91 -23\n-22 66') == 'War'
    assert solve('5 3 6 8\n-10 3 1 5 -100\n100 6 14') == 'War'
