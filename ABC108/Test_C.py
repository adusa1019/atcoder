import pytest
from C import solve


def test_solve():
    assert solve('3 2') == '9'
    assert solve('5 3') == '1'
    assert solve('31415 9265') == '27'
    assert solve('35897 932') == '114191'
