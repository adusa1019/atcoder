import pytest
from A import solve


def test_solve():
    assert solve('2019/04/30') == 'Heisei'
    assert solve('2019/11/01') == 'TBD'
