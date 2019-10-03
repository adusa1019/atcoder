import pytest
from A import solve


def test_solve():
    assert solve('3776') == 'Bad'
    assert solve('8080') == 'Good'
    assert solve('1333') == 'Bad'
    assert solve('0024') == 'Bad'
