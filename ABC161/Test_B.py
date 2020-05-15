import pytest
from B import solve


def test_solve():
    assert solve('4 1\n5 4 2 1') == 'Yes'
    assert solve('3 2\n380 19 1') == 'No'
    assert solve('12 3\n4 56 78 901 2 345 67 890 123 45 6 789') == 'Yes'
