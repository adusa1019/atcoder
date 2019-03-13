import pytest
from A import solve


def test_solve():
    assert solve('+-++') == '2'
    assert solve('-+--') == '-2'
    assert solve('----') == '-4'
