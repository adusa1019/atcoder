import pytest
from B import solve


def test_solve():
    assert solve('cabacc\nabc') == '1'
    assert solve('codeforces\natcoder') == '6'
