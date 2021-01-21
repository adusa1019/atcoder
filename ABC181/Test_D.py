import pytest
from D import solve


def test_solve():
    assert solve('1234') == 'Yes'
    assert solve('1333') == 'No'
    assert solve('8') == 'Yes'
