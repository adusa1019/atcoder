import pytest
from B import solve


def test_solve():
    assert solve('AtCoder') == 'AC'
    assert solve('ACoder') == 'WA'
    assert solve('AcycliC') == 'WA'
    assert solve('AtCoCo') == 'WA'
    assert solve('Atcoder') == 'WA'
