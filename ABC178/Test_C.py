import pytest
from C import solve


def test_solve():
    assert solve('2') == '2'
    assert solve('1') == '0'
    assert solve('869121') == '2511445'
