import pytest
from C import solve


def test_solve():
    assert solve('5\nWEEWW') == '1'
    assert solve('12\nWEWEWEEEWWWE') == '4'
    assert solve('8\nWWWWWEEE') == '3'
