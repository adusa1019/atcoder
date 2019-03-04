import pytest
from C import solve


def test_solve():
    assert solve('1214\n4') == '2'
    assert solve('3\n157') == '3'
    assert solve('299792458\n9460730472580800') == '2'
    assert solve('112\n2') == '1'
    assert solve('113\n3') == '3'
