import pytest
from B import solve


def test_solve():
    assert solve('2\nABCXYZ') == 'CDEZAB'
    assert solve('0\nABCXYZ') == 'ABCXYZ'
    assert solve('13\nABCDEFGHIJKLMNOPQRSTUVWXYZ') == 'NOPQRSTUVWXYZABCDEFGHIJKLM'
