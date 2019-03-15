import pytest
from B import solve


def test_solve():
    assert solve('6\naabbca') == '2'
    assert solve('10\naaaaaaaaaa') == '1'
    assert solve('45\ntgxgdqkyjzhyputjjtllptdfxocrylqfqjynmfbfucbir') == '9'
