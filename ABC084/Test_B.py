import pytest
from B import solve


def test_solve():
    assert solve('3 4\n269-6650') == 'Yes'
    assert solve('1 1\n---') == 'No'
    assert solve('1 2\n7444') == 'No'
