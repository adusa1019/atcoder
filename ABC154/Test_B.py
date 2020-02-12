import pytest
from B import solve


def test_solve():
    assert solve('sardine') == 'xxxxxxx'
    assert solve('xxxx') == 'xxxx'
    assert solve('gone') == 'xxxx'
