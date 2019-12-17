import pytest
from B import solve


def test_solve():
    assert solve('redcoder') == '1'
    assert solve('vvvvvv') == '0'
    assert solve('abcdabc') == '2'
