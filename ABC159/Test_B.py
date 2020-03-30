import pytest
from B import solve


def test_solve():
    assert solve('akasaka') == 'Yes'
    assert solve('level') == 'No'
    assert solve('atcoder') == 'No'
