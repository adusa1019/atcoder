import pytest
from B import solve


def test_solve():
    assert solve('6\nabcabc') == 'Yes'
    assert solve('6\nabcadc') == 'No'
    assert solve('1\nz') == 'No'
