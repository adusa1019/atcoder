import pytest
from B import solve


def test_solve():
    assert solve('2\n10000 JPY\n0.10000000 BTC') == '48000.0'
    assert solve('3\n100000000 JPY\n100.00000000 BTC\n0.00000001 BTC') == '138000000.0038'
