import pytest
from B import solve


def test_solve():
    assert solve('3\n3 1 2\n2 5 4\n3 6') == '14'
    assert solve('4\n2 3 4 1\n13 5 8 24\n45 9 15') == '74'
    assert solve('2\n1 2\n50 50\n50') == '150'
