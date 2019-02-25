import pytest
from C import solve


def test_solve():
    assert solve('575') == '4'
    assert solve('3600') == '13'
    assert solve('999999999') == '26484'
