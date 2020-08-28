import pytest
from B import solve


def test_solve():
    assert solve('123456789') == 'Yes'
    assert solve('0') == 'Yes'
    assert solve('31415926535897932384626433832795028841971693993751058209749445923078164062862089986280') == 'No'
