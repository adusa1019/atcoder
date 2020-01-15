import pytest
from B import solve


def test_solve():
    assert solve('10\nZABCDBABCQ') == '2'
    assert solve('19\nTHREEONEFOURONEFIVE') == '0'
    assert solve('33\nABCCABCBABCCABACBCBBABCBCBCBCABCB') == '5'
