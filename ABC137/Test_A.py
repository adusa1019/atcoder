import pytest
from A import solve


def test_solve():
    assert solve('-13 3') == '-10'
    assert solve('1 -33') == '34'
    assert solve('13 3') == '39'
