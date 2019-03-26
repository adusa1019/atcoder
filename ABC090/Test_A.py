import pytest
from A import solve


def test_solve():
    assert solve('ant\nobe\nrec') == 'abc'
    assert solve('edu\ncat\nion') == 'ean'
