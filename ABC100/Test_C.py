import pytest
from C import solve


def test_solve():
    assert solve('3\n5 2 4') == '3'
    assert solve('4\n631 577 243 199') == '0'
    assert solve('10\n2184 2126 1721 1800 1024 2528 3360 1945 1280 1776') == '39'
