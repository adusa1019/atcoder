import pytest
from D import solve


def test_solve():
    assert solve('4\n1 2 3 4\n3\n1 2\n3 4\n2 4') == '11\n12\n16'
    assert solve('4\n1 1 1 1\n3\n1 2\n2 1\n3 5') == '8\n4\n4'
    assert solve('2\n1 2\n3\n1 100\n2 100\n100 1000') == '102\n200\n2000'
