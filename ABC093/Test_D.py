import pytest
from D import solve


def test_solve():
    assert solve('8\n1 4\n10 5\n3 3\n4 11\n8 9\n22 40\n8 36\n314159265 358979323') == '1\n12\n4\n11\n14\n57\n31\n671644785'
