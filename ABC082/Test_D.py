import pytest
from D import solve


def test_solve():
    assert solve('FTFFTFFF\n4 2') == 'Yes'
    assert solve('FTFFTFFF\n-2 -2') == 'Yes'
    assert solve('FF\n1 0') == 'No'
    assert solve('TF\n1 0') == 'No'
    assert solve('FFTTFF\n0 0') == 'Yes'
    assert solve('TTTT\n1 0') == 'No'
