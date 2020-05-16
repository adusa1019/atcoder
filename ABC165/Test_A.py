import pytest
from A import solve


def test_solve():
    assert solve('7\n500 600') == 'OK'
    assert solve('4\n5 7') == 'NG'
    assert solve('1\n11 11') == 'OK'
