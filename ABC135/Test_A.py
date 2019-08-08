import pytest
from A import solve


def test_solve():
    assert solve('2 16') == '9'
    assert solve('0 3') == 'IMPOSSIBLE'
    assert solve('998244353 99824435') == '549034394'
