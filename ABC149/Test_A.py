import pytest
from A import solve


def test_solve():
    assert solve('oder atc') == 'atcoder'
    assert solve('humu humu') == 'humuhumu'
