import pytest
from C import solve


def test_solve():
    assert solve('2\n3 4') == '3.5'
    assert solve('3\n500 300 200') == '375.0'
    assert solve('5\n138 138 138 138 138') == '138.0'
