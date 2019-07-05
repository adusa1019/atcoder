import pytest
from C import solve


def test_solve():
    assert solve('3 10') == '0.145833333333'
    assert solve('100000 5') == '0.999973749998'
