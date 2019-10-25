import pytest
from C import solve


def test_solve():
    assert solve('10\naabbbbaaca') == '5'
    assert solve('5\naaaaa') == '1'
    assert solve('20\nxxzaffeeeeddfkkkkllq') == '10'
