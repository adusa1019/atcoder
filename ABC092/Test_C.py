import pytest
from C import solve


def test_solve():
    assert solve('3\n3 5 -1') == '12\n8\n10'
    assert solve('5\n1 1 1 2 0') == '4\n4\n4\n2\n4'
    assert solve('6\n-679 -2409 -3258 3095 -3291 -4462') == '21630\n21630\n19932\n8924\n21630\n19288'
