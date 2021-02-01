import pytest
from D import solve


def test_solve():
    assert solve('4 10\n1 3 5\n2 4 4\n3 10 6\n2 4 1') == 'No'
    assert solve('4 10\n1 3 5\n2 4 4\n3 10 6\n2 3 1') == 'Yes'
    assert solve('6 1000000000\n0 200000 999999999\n2 20 1\n20 200 1\n200 2000 1\n2000 20000 1\n20000 200000 1') == 'Yes'
