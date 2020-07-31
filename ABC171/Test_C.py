import pytest
from C import solve


def test_solve():
    assert solve('2') == 'b'
    assert solve('26') == 'z'
    assert solve('27') == 'aa'
    assert solve('702') == 'zz'
    assert solve('123456789') == 'jjddja'
