import pytest
from C import solve


def test_solve():
    assert solve('3\n6 5 1\n1 10 1') == '12\n11\n0'
    assert solve('4\n12 24 6\n52 16 4\n99 2 2') == '187\n167\n101\n0'
    assert solve('4\n12 13 1\n44 17 17\n66 4096 64') == '4162\n4162\n4162\n0'
