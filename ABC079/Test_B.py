import pytest
from B import solve


def test_solve():
    assert solve('5') == '11'
    assert solve('86') == '939587134549734843'
