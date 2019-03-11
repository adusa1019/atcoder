import pytest
from B import solve


def test_solve():
    assert solve('kyoto\ntokyo') == 'Yes'
    assert solve('abc\narc') == 'No'
    assert solve('aaaaaaaaaaaaaaab\naaaaaaaaaaaaaaab') == 'Yes'
