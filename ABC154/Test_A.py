import pytest
from A import solve


def test_solve():
    assert solve('red blue\n3 4\nred') == '2 4'
    assert solve('red blue\n5 5\nblue') == '5 4'
