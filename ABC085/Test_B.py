import pytest
from B import solve


def test_solve():
    assert solve('4\n10\n8\n8\n6') == '3'
    assert solve('3\n15\n15\n15') == '1'
    assert solve('7\n50\n30\n50\n100\n50\n80\n30') == '4'
