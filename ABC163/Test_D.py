import pytest
from D import solve


def test_solve():
    assert solve('3 2') == '10'
    assert solve('200000 200001') == '1'
    assert solve('141421 35623') == '220280457'
    assert solve('200000 1') == '324266530'
