import pytest
from B import solve


def test_solve():
    assert solve('3\n4980\n7980\n6980') == '15950'
    assert solve('4\n4320\n4320\n4320\n4320') == '15120'
