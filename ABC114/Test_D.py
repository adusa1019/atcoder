import pytest
from D import solve


def test_solve():
    assert solve('9') == '0'
    assert solve('10') == '1'
    assert solve('100') == '543'
