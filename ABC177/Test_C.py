import pytest
from C import solve


def test_solve():
    assert solve('3\n1 2 3') == '11'
    assert solve('4\n141421356 17320508 22360679 244949') == '437235829'
