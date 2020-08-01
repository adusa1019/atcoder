import pytest
from B import solve


def test_solve():
    assert solve('6\nAC\nTLE\nAC\nAC\nWA\nTLE') == 'AC x 3\nWA x 1\nTLE x 2\nRE x 0'
    assert solve('10\nAC\nAC\nAC\nAC\nAC\nAC\nAC\nAC\nAC\nAC') == 'AC x 10\nWA x 0\nTLE x 0\nRE x 0'
