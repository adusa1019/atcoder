import pytest
from B import solve


def test_solve():
    assert solve('1 21') == 'Yes'
    assert solve('100 100') == 'No'
    assert solve('12 10') == 'No'
