import pytest
from A import solve


def test_solve():
    assert solve('ABA') == 'Yes'
    assert solve('BBA') == 'Yes'
    assert solve('BBB') == 'No'
