import pytest
from A import solve


def test_solve():
    assert solve('117') == 'Yes'
    assert solve('123') == 'No'
    assert solve('777') == 'Yes'
