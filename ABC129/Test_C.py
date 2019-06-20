import pytest
from C import solve


def test_solve():
    assert solve('6 1\n3') == '4'
    assert solve('10 2\n4\n5') == '0'
    assert solve('100 5\n1\n23\n45\n67\n89') == '608200469'
