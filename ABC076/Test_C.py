import pytest
from C import solve


def test_solve():
    assert solve('?tc????\ncoder') == 'atcoder'
    assert solve('??p??d??\nabc') == 'UNRESTORABLE'
