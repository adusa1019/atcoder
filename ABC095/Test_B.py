import pytest
from B import solve


def test_solve():
    assert solve('3 1000\n120\n100\n140') == '9'
    assert solve('4 360\n90\n90\n90\n90') == '4'
    assert solve('5 3000\n150\n130\n150\n130\n110') == '26'
