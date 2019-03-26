import pytest
from C import solve


def test_solve():
    assert solve('5\nMASHIKE\nRUMOI\nOBIRA\nHABORO\nHOROKANAI') == '2'
    assert solve('4\nZZ\nZZZ\nZ\nZZZZZZZZZZ') == '0'
    assert solve('5\nCHOKUDAI\nRNG\nMAKOTO\nAOKI\nRINGO') == '7'
