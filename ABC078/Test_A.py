import pytest
from A import solve


def test_solve():
    assert solve('A B') == '<'
    assert solve('E C') == '>'
    assert solve('F F') == '='
