import pytest
from C import solve


def test_solve():
    assert solve('3\nacornistnt\npeanutbomb\nconstraint') == '1'
    assert solve('2\noneplustwo\nninemodsix') == '0'
    assert solve('5\nabaaaaaaaa\noneplustwo\naaaaaaaaba\ntwoplusone\naaaabaaaaa') == '4'
