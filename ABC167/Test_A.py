import pytest
from A import solve


def test_solve():
    assert solve('chokudai\nchokudaiz') == 'Yes'
    assert solve('snuke\nsnekee') == 'No'
    assert solve('a\naa') == 'Yes'
