import pytest
from A import solve


def test_solve():
    assert solve('1 5 2') == '53'
    assert solve('9 9 9') == '108'
    assert solve('6 6 7') == '82'
