import pytest
from B import solve


def test_solve():
    assert solve('103') == '3'
    assert solve('1000000000000000000') == '3760'
    assert solve('1333333333') == '1706'
