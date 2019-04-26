import pytest
from C import solve


def test_solve():
    assert solve('-9') == '1011'
    assert solve('13') == '11101'
    assert solve('123456789') == '11000101011001101110100010101'
    assert solve('0') == '0'
