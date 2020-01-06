import pytest
from D import solve


def test_solve():
    assert solve('5 2\n8 7 6\nrsrpr') == '27'
    assert solve('7 1\n100 10 1\nssssppr') == '211'
    assert solve('30 5\n325 234 123\nrspsspspsrpspsppprpsprpssprpsr') == '4996'
