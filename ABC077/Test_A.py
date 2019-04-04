import pytest
from A import solve


def test_solve():
    assert solve('pot\ntop') == 'YES'
    assert solve('tab\nbet') == 'NO'
    assert solve('eye\neel') == 'NO'
