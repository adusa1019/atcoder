import pytest
from A import solve


def test_solve():
    assert solve('2017/01/07') == '2018/01/07'
    assert solve('2017/01/31') == '2018/01/31'
