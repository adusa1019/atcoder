import pytest
from C import solve


def test_solve():
    assert solve('3\napple\norange\napple') == '2'
    assert solve('5\ngrape\ngrape\ngrape\ngrape\ngrape') == '1'
    assert solve('4\naaaa\na\naaa\naa') == '4'
