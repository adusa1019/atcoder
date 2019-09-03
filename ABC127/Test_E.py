import pytest
from E import solve


def test_solve():
    assert solve('2 2 2') == '8'
    assert solve('4 5 4') == '87210'
    assert solve('100 100 5000') == '817260251'
    assert solve('200 200 10000') == '474603202'
    assert solve('200 200 30000') == '718758288'
