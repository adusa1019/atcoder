import pytest
from C import solve


def test_solve():
    assert solve('azzel\napple') == 'Yes'
    assert solve('chokudai\nredcoder') == 'No'
    assert solve('abcdefghijklmnopqrstuvwxyz\nibyhqfrekavclxjstdwgpzmonu') == 'Yes'
