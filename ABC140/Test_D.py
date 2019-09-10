import pytest
from D import solve


def test_solve():
    assert solve('6 1\nLRLRRL') == '3'
    assert solve('13 3\nLRRLRLRRLRLLR') == '9'
    assert solve('10 1\nLLLLLRRRRR') == '9'
    assert solve('9 2\nRRRLRLRLL') == '7'
