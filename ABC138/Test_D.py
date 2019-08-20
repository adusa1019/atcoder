import pytest
from D import solve


def test_solve():
    assert solve('4 3\n1 2\n2 3\n2 4\n2 10\n1 100\n3 1') == '100 110 111 110'
    assert solve('6 2\n1 2\n1 3\n2 4\n3 6\n2 5\n1 10\n1 10') == '20 20 20 20 20 20'
