import pytest
from D import solve


def test_solve():
    assert solve('4 5\n3 2 4 1') == '4'
    assert solve('4 1\n3 2 4 1') == '3'
    assert solve('6 727202214173249351\n6 5 2 5 3 2') == '2'
